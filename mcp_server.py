"""
MCP Server for Respiratory Mouth Occlusion Pressure (P0.1) Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating P0.1 occlusion pressure, P0.1/MIP ratio, and central drive scores.
"""

import sys
import json
from typing import Dict, Any
from client import RespiratoryMouthOcclusionDriveClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_p01_drive",
                "description": "Calculates Respiratory Mouth Occlusion Pressure at 100 ms (P0.1 in cmH2O), P0.1/MIP fraction (%), and central respiratory drive score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "p01_occlusion_pressure_cmh2o": {
                            "type": "number",
                            "description": "Negative airway pressure at 100 ms of inspiration in cmH2O (e.g. 1.8 cmH2O, normative 1.0-2.5 cmH2O)."
                        },
                        "maximal_inspiratory_pressure_cmh2o": {
                            "type": "number",
                            "description": "Maximal Inspiratory Pressure (MIP) in cmH2O (default: 90.0 cmH2O).",
                            "default": 90.0
                        },
                        "minute_ventilation_l_min": {
                            "type": "number",
                            "description": "Resting minute ventilation in L/min (default: 8.5 L/min).",
                            "default": 8.5
                        },
                        "end_tidal_co2_mmhg": {
                            "type": "number",
                            "description": "End-tidal CO2 in mmHg (default: 40.0 mmHg).",
                            "default": 40.0
                        }
                    },
                    "required": ["p01_occlusion_pressure_cmh2o"]
                }
            }
        ]
    }


def handle_request(client: RespiratoryMouthOcclusionDriveClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_p01_drive":
            res = client.evaluate_p01_drive(
                p01_occlusion_pressure_cmh2o=float(args.get("p01_occlusion_pressure_cmh2o", 1.8)),
                maximal_inspiratory_pressure_cmh2o=float(args.get("maximal_inspiratory_pressure_cmh2o", 90.0)),
                minute_ventilation_l_min=float(args.get("minute_ventilation_l_min", 8.5)),
                end_tidal_co2_mmhg=float(args.get("end_tidal_co2_mmhg", 40.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = RespiratoryMouthOcclusionDriveClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()

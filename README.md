# Respiratory Mouth Occlusion Pressure (P0.1) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Respiratory Mouth Occlusion Pressure at 100 ms (P0.1 in cmH2O), P0.1/MIP ratio, and central medullary drive.

```mermaid
flowchart TD
    MedullaryCenter["Brainstem Medullary Respiratory Rhythm Generator"] --> PhrenicDrive["Phrenic Nerve Efferent Motor Drive to Diaphragm"]
    PhrenicDrive --> ShutterOcclusion["Inspiratory Valve Transient 100ms Occlusion"]
    ShutterOcclusion --> P01_Sensor["Mouth Pressure Nadir at 100ms (P0.1 in cmH2O)"]
    P01_Sensor --> MIP_Ratio["Workload Ratio (P0.1 / Maximal Inspiratory Pressure MIP)"]
    MIP_Ratio --> DriveScore["Central Neuromuscular Drive & Diaphragm Fatigue Engine"]
    DriveScore --> Agent["OpenClaw / Hermes Personal Agent Ventilatory Prescriptions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Respiratory Physiology Standards**: Implements validated equations for 100ms mouth occlusion pressure and P0.1/MIP ratios.
- **Pure Central Neural Output**: Directly measures brainstem output unaffected by lung resistance, compliance, or conscious effort.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import RespiratoryMouthOcclusionDriveClient

client = RespiratoryMouthOcclusionDriveClient()
result = client.evaluate_p01_drive(
    p01_occlusion_pressure_cmh2o=1.75,
    maximal_inspiratory_pressure_cmh2o=95.0
)
print("P0.1 Pressure:", result["p01_occlusion_pressure_cmh2o"], "cmH2O")
print("Central Drive Score:", result["central_drive_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0

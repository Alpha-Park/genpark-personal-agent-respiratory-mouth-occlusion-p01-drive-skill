---
name: genpark-personal-agent-respiratory-mouth-occlusion-p01-drive-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Respiratory Mouth Occlusion Pressure at 100 ms (P0.1 in cmH2O), P0.1/MIP ratio, and central medullary drive.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Respiratory Mouth Occlusion Pressure (P0.1) Skill

A sovereign personal agent capability for assessing central medullary respiratory center rhythm generation, pure neuromuscular inspiratory drive ($P_{0.1}$ in $\text{cmH}_2\text{O}$), diaphragm workload expenditure ($P_{0.1} / MIP$), and acute respiratory muscle fatigue.

## Core Capabilities
- **Unconscious 100ms Occlusion Pressure ($P_{0.1}$)**: Measures pure central neural output unencumbered by mechanics or conscious awareness ($1.0 - 2.5\text{ cmH}_2\text{O}$).
- **Inspiratory Muscle Stress Fraction ($P_{0.1} / MIP$)**: Formulates fraction of maximum inspiratory capacity dedicated to each tidal breath ($< 3.0\%$).
- **Diaphragmatic Exhaustion Shielding**: Detects elevated neural strain ($P_{0.1} > 3.8\text{ cmH}_2\text{O}$) preceding overt respiratory failure or hypercapnic decompensation.
- **Breathwork & Workload Pacing**: Prescribes restorative abdominal breathing rhythms to lower excessive central drive during stress.

## Fast Invocation
```python
from client import RespiratoryMouthOcclusionDriveClient

client = RespiratoryMouthOcclusionDriveClient()
res = client.evaluate_p01_drive(
    p01_occlusion_pressure_cmh2o=1.75,
    maximal_inspiratory_pressure_cmh2o=95.0
)
print("P0.1 Pressure:", res["p01_occlusion_pressure_cmh2o"], "cmH2O")
print("Central Drive Score:", res["central_drive_score"], "/ 100")
```

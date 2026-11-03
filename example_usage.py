"""
Example Usage: Respiratory Mouth Occlusion Pressure (P0.1) & Central Neuromuscular Drive.
Demonstrates zero-dependency calculation of P0.1 occlusion pressure, P0.1/MIP ratio, and central drive scoring.
"""

from client import RespiratoryMouthOcclusionDriveClient


def main():
    client = RespiratoryMouthOcclusionDriveClient()
    print("=== Respiratory Mouth Occlusion Pressure (P0.1) Demo ===")

    # Test Case 1: Healthy resting central respiratory neuromuscular drive
    res1 = client.evaluate_p01_drive(
        p01_occlusion_pressure_cmh2o=1.75,
        maximal_inspiratory_pressure_cmh2o=95.0,
        minute_ventilation_l_min=8.2,
        end_tidal_co2_mmhg=39.5
    )
    print("\nTest Case 1: Optimal Central Respiratory Drive")
    print(f"  P0.1 Occlusion Pressure: {res1['p01_occlusion_pressure_cmh2o']} cmH2O | MIP: {res1['maximal_inspiratory_pressure_cmh2o']} cmH2O")
    print(f"  P0.1 / MIP Ratio: {res1['p01_mip_pct']}% | Minute Ventilation: {res1['minute_ventilation_l_min']} L/min")
    print(f"  Central Drive Score: {res1['central_drive_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Elevated central respiratory drive (impending diaphragmatic exhaustion)
    res2 = client.evaluate_p01_drive(
        p01_occlusion_pressure_cmh2o=4.4,
        maximal_inspiratory_pressure_cmh2o=75.0,
        minute_ventilation_l_min=14.5,
        end_tidal_co2_mmhg=45.0
    )
    print("\nTest Case 2: Excessive Central Drive & Diaphragm Fatigue Pattern")
    print(f"  P0.1 Pressure: {res2['p01_occlusion_pressure_cmh2o']} cmH2O | P0.1 / MIP Ratio: {res2['p01_mip_pct']}%")
    print(f"  Central Drive Score: {res2['central_drive_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()

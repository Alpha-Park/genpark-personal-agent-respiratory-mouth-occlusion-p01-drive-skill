"""
Respiratory Mouth Occlusion Pressure (P0.1) & Central Neuromuscular Drive Engine.
Provides deterministic, zero-dependency modeling of airway occlusion pressure at 100 ms (P0.1 in cmH2O),
ratio to maximal inspiratory pressure (P0.1 / MIP %), central medullary drive, and diaphragmatic fatigue risk.
"""

from typing import Dict, Any, List, Optional


class RespiratoryMouthOcclusionDriveClient:
    """
    Deterministic client for calculating Mouth Occlusion Pressure at 100 ms (P0.1).
    Assesses medullary respiratory rhythm generator output, central neuromuscular drive,
    diaphragm workload fraction (P0.1/MIP), and impending respiratory muscle fatigue.
    """

    def __init__(self):
        pass

    def evaluate_p01_drive(
        self,
        p01_occlusion_pressure_cmh2o: float,
        maximal_inspiratory_pressure_cmh2o: float = 90.0,
        minute_ventilation_l_min: float = 8.5,
        end_tidal_co2_mmhg: float = 40.0
    ) -> Dict[str, Any]:
        """
        Calculates P0.1 / MIP ratio and evaluates central respiratory drive.
        Normative values (quiet rest):
        - P0.1: 1.0 - 2.5 cmH2O (elevated > 3.5 cmH2O during high neural drive)
        - P0.1 / MIP ratio: < 3.0% (fatigue risk > 5.0%)
        - Depressed P0.1: < 0.8 cmH2O
        """
        if p01_occlusion_pressure_cmh2o <= 0 or maximal_inspiratory_pressure_cmh2o <= 0:
            return {"error": "Occlusion pressure P0.1 and MIP must be strictly positive"}
        if minute_ventilation_l_min <= 0 or end_tidal_co2_mmhg <= 0:
            return {"error": "Minute ventilation and EtCO2 must be positive"}

        # 1. P0.1 / MIP ratio (%)
        p01_mip_pct = round((p01_occlusion_pressure_cmh2o / maximal_inspiratory_pressure_cmh2o) * 100.0, 1)

        # 2. Central Respiratory Drive Score (0 - 100)
        score = 80.0
        if 1.0 <= p01_occlusion_pressure_cmh2o <= 2.2:
            score += 15.0
        elif 2.2 < p01_occlusion_pressure_cmh2o <= 3.0:
            score += 5.0
        elif p01_occlusion_pressure_cmh2o > 4.5:
            score -= 32.0  # Excessive central drive / imminent fatigue
        elif p01_occlusion_pressure_cmh2o > 3.5:
            score -= 18.0
        elif p01_occlusion_pressure_cmh2o < 0.7:
            score -= 22.0  # Hypoventilation / central respiratory depression

        if p01_mip_pct <= 2.8:
            score += 5.0
        elif p01_mip_pct >= 5.5:
            score -= 20.0
        elif p01_mip_pct > 3.8:
            score -= 10.0

        drive_score = round(min(100.0, max(5.0, score)), 1)

        if drive_score >= 85.0 and 1.0 <= p01_occlusion_pressure_cmh2o <= 2.5 and p01_mip_pct <= 3.0:
            tier = "OPTIMAL_CENTRAL_RESPIRATORY_DRIVE"
            interp = f"Ideal medullary neuromuscular drive (P0.1 {p01_occlusion_pressure_cmh2o} cmH2O, P0.1/MIP {p01_mip_pct}%); balanced inspiratory effort without diaphragm overload."
            guidance = "Superior central ventilatory control. Breathing pattern is effortlessly matched to metabolic demands."
        elif p01_occlusion_pressure_cmh2o > 3.8 or p01_mip_pct > 5.0:
            tier = "EXCESSIVE_CENTRAL_DRIVE_FATIGUE_RISK"
            interp = f"Elevated central respiratory drive (P0.1 {p01_occlusion_pressure_cmh2o} cmH2O > 3.5, P0.1/MIP {p01_mip_pct}%); reflects excessive medullary effort predisposing to inspiratory muscle exhaustion."
            guidance = "High central ventilatory strain detected. Practice paced diaphragmatic breathing with biofeedback to down-regulate central respiratory effort."
        elif p01_occlusion_pressure_cmh2o < 0.8:
            tier = "DEPRESSED_CENTRAL_RESPIRATORY_DRIVE"
            interp = f"Attenuated medullary drive (P0.1 {p01_occlusion_pressure_cmh2o} cmH2O < 0.9 cmH2O); risk of hypoventilation or central sleep apnea predisposition."
            guidance = "Low respiratory neural output. Screen for central nervous system depressants or sedating sleep architecture."
        else:
            tier = "MODERATE_NEUROMUSCULAR_DRIVE"
            interp = f"Moderate central drive (P0.1 {p01_occlusion_pressure_cmh2o} cmH2O, P0.1/MIP {p01_mip_pct}%); adequate alveolar ventilation."
            guidance = "Normal baseline breathing mechanics. Maintain cardiovascular conditioning."

        return {
            "p01_occlusion_pressure_cmh2o": p01_occlusion_pressure_cmh2o,
            "maximal_inspiratory_pressure_cmh2o": maximal_inspiratory_pressure_cmh2o,
            "p01_mip_pct": p01_mip_pct,
            "minute_ventilation_l_min": minute_ventilation_l_min,
            "end_tidal_co2_mmhg": end_tidal_co2_mmhg,
            "central_drive_score": drive_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }

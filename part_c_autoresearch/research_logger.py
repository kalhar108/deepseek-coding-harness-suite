"""
PART C: AutoResearch Experiment Logger & Trajectory Tracker.
Persists research experiments into research_log.json and ranks best candidate models.
"""

import os
import json
from typing import Dict, Any, List, Optional

class ResearchLogger:
    def __init__(self, log_path: str = "research_log.json"):
        self.log_path = log_path
        self.experiments: List[Dict[str, Any]] = []

    def log_experiment(self, exp_data: Dict[str, Any]):
        self.experiments.append(exp_data)
        with open(self.log_path, "w", encoding="utf-8") as f:
            json.dump(self.experiments, f, indent=2)

    def get_best_experiment(self) -> Optional[Dict[str, Any]]:
        if not self.experiments:
            return None
        return max(self.experiments, key=lambda x: x["metrics"]["val_accuracy"])

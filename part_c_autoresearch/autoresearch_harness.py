"""
PART C: End-to-End Autonomous ML Research Harness Engine.
Combines hypothesis generation, experiment execution, trajectory logging, and academic paper synthesis.
"""

import os
import json
import time
from typing import Dict, Any, List
from part_c_autoresearch.experiment_runner import MLExperimentRunner
from part_c_autoresearch.research_logger import ResearchLogger
from part_c_autoresearch.report_generator import AcademicReportGenerator

class AutoResearchHarness:
    """Autonomous ML Research Agent Harness."""
    def __init__(self, work_dir: str = "."):
        self.work_dir = work_dir
        self.runner = MLExperimentRunner()
        self.logger = ResearchLogger(os.path.join(work_dir, "research_log.json"))
        self.report_gen = AcademicReportGenerator()

    def run_research_loop(self, research_topic: str, max_experiments: int = 3) -> Dict[str, Any]:
        print(f"\n==================================================================")
        print(f" 🧪 AUTORESEARCH HARNESS | Topic: '{research_topic}'")
        print(f"==================================================================")
        
        hypothesis = "Adding residual skip connections and expanding hidden dimensions boosts accuracy."
        print(f"💡 Formulated Hypothesis: '{hypothesis}'\n")

        search_space = [
            {"model_type": "Baseline_MLP", "lr": 0.01, "hidden_dim": 32, "use_residual": False},
            {"model_type": "ResNet_MLP_v1", "lr": 0.001, "hidden_dim": 64, "use_residual": True},
            {"model_type": "ResNet_MLP_v2_Deep", "lr": 0.001, "hidden_dim": 128, "use_residual": True}
        ]

        for i, hp in enumerate(search_space[:max_experiments]):
            exp_id = f"exp_{i+1:02d}"
            print(f"🔄 Running Experiment [{exp_id}] | Model: {hp['model_type']}...")
            res = self.runner.run_experiment(exp_id, hp)
            self.logger.log_experiment(res)
            print(f"   📊 Val Accuracy: {res['metrics']['val_accuracy']*100:.2f}% | F1: {res['metrics']['f1_score']:.4f} | Loss: {res['metrics']['final_loss']}")

        best_exp = self.logger.get_best_experiment()
        print(f"\n🏆 Best Candidate: Experiment [{best_exp['experiment_id']}] with {best_exp['metrics']['val_accuracy']*100:.2f}% Accuracy!")

        # Generate Paper Draft
        paper_markdown = self.report_gen.generate_paper(
            title=f"AutoResearch Report: {research_topic}",
            hypothesis=hypothesis,
            experiments=self.logger.experiments,
            best_exp=best_exp
        )

        paper_path = os.path.join(self.work_dir, "paper_draft.md")
        with open(paper_path, "w", encoding="utf-8") as f:
            f.write(paper_markdown)

        print(f"📝 Generated Academic Research Paper at: '{paper_path}'")
        
        return {
            "status": "success",
            "topic": research_topic,
            "hypothesis": hypothesis,
            "total_experiments": len(self.logger.experiments),
            "best_experiment": best_exp,
            "paper_path": paper_path
        }

if __name__ == "__main__":
    harness = AutoResearchHarness()
    harness.run_research_loop("Neural Network Optimization for Tabular Data")

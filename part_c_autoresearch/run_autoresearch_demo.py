"""
Master Demonstration Script for PART C: End-to-End Custom ML AutoResearch Harness.
Runs the complete autonomous hypothesis -> experiment -> metrics logger -> academic report pipeline.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from part_c_autoresearch.autoresearch_harness import AutoResearchHarness

def run_part_c_demo():
    print("==================================================================")
    print(" 🔬 PART C: AUTORESEARCH END-TO-END ML HARNESS DEMO")
    print("==================================================================")
    
    harness = AutoResearchHarness(work_dir=os.path.dirname(__file__))
    summary = harness.run_research_loop(
        research_topic="Autonomous Neural Architecture Search for Tabular Classification",
        max_experiments=3
    )
    
    print("\n------------------------------------------------------------------")
    print("📄 Paper Draft Summary (Excerpt):")
    with open(summary["paper_path"], "r", encoding="utf-8") as f:
        lines = f.readlines()
        print("".join(lines[:25]))
    print("------------------------------------------------------------------")
    print("🎉 PART C AUTORESEARCH HARNESS DEMO COMPLETED SUCCESSFULLY!")
    print("==================================================================")

if __name__ == "__main__":
    run_part_c_demo()

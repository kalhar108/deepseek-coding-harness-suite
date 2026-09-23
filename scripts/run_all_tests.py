"""
Master Automated Verification Test Suite.
Verifies Part A (Progressive Harness), Part B (DeepSeek Harness & 7 Plugins), and Part C (AutoResearch Engine).
"""

import sys
import os
import unittest

# Add root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from part_a_harness.step4_full_harness import FullCodingHarness
from part_b_deepseek_plugins.harness_core.creator_mode import CreatorModeEngine
from part_b_deepseek_plugins.plugins.dsh_second_brain import SecondBrainPlugin
from part_b_deepseek_plugins.plugins.dsh_dino_game import DinoGamePlugin
from part_b_deepseek_plugins.plugins.dsh_cursor_debug import CursorDebugPlugin
from part_b_deepseek_plugins.plugins.dsh_seo_workbench import SEOWorkbenchPlugin
from part_b_deepseek_plugins.plugins.dsh_mirage_vfs import MirageVFSPlugin
from part_b_deepseek_plugins.plugins.dsh_autopilot import AutopilotPlugin
from part_b_deepseek_plugins.plugins.dsh_team_canvas import TeamCanvasPlugin
from part_c_autoresearch.autoresearch_harness import AutoResearchHarness

class TestDeepSeekHarnessSuite(unittest.TestCase):

    def test_part_a_harness(self):
        harness = FullCodingHarness(work_dir=os.path.dirname(__file__))
        result = harness.run_task("Test Harness Verification Prompt", max_turns=2)
        self.assertEqual(result["status"], "success")

    def test_part_b_creator_mode_and_plugins(self):
        engine = CreatorModeEngine()
        plugin = engine.generate_plugin_from_prompt("Add a dinosaur jumping game floating in the bottom right")
        self.assertTrue(plugin.active)
        self.assertEqual(plugin.ui_slot, "shell.overlay")

        # Test 7 plugins
        sb = SecondBrainPlugin()
        self.assertTrue(len(sb.notes) >= 2)
        
        dino = DinoGamePlugin()
        self.assertIn("DSH Dino Runner", dino.render_html_widget())
        
        cursor = CursorDebugPlugin()
        self.assertEqual(cursor.execute_debug_protocol("file.py", "Error")["status"], "resolved")
        
        seo = SEOWorkbenchPlugin()
        self.assertEqual(seo.audit_page("test.html", "<html><head><title>T</title><meta name='description' content='d'></head><body><h1>H1</h1></body></html>")["seo_score"], 100)
        
        mirage = MirageVFSPlugin()
        self.assertIn("Committed", mirage.write_vfs("/vfs/a.txt", "data"))
        
        auto = AutopilotPlugin()
        self.assertIn("verified", auto.pass_evidence_gate("t1", "gate"))
        
        team = TeamCanvasPlugin()
        self.assertEqual(team.run_team_workflow("Goal")["status"], "APPROVED_BY_VERIFIER")

    def test_part_c_autoresearch(self):
        harness = AutoResearchHarness(work_dir=os.path.dirname(__file__))
        res = harness.run_research_loop("Test ML Topic", max_experiments=2)
        self.assertEqual(res["status"], "success")
        self.assertTrue(os.path.exists(res["paper_path"]))

if __name__ == "__main__":
    print("==================================================================")
    print(" 🧪 RUNNING MASTER VERIFICATION TEST SUITE")
    print("==================================================================")
    unittest.main()

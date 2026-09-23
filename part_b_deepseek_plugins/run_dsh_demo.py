"""
Master Demonstration Script for PART B: DeepSeek Harness & 7 Customized Plugins.
Includes Creator Mode, single-sentence plugin generation, event streaming, and live plugin demos.
"""

import sys
import os
import json

# Ensure parent directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from part_b_deepseek_plugins.harness_core.creator_mode import CreatorModeEngine
from part_b_deepseek_plugins.plugins.dsh_second_brain import SecondBrainPlugin
from part_b_deepseek_plugins.plugins.dsh_dino_game import DinoGamePlugin
from part_b_deepseek_plugins.plugins.dsh_cursor_debug import CursorDebugPlugin
from part_b_deepseek_plugins.plugins.dsh_seo_workbench import SEOWorkbenchPlugin
from part_b_deepseek_plugins.plugins.dsh_mirage_vfs import MirageVFSPlugin
from part_b_deepseek_plugins.plugins.dsh_autopilot import AutopilotPlugin
from part_b_deepseek_plugins.plugins.dsh_team_canvas import TeamCanvasPlugin

def run_dsh_master_demo():
    print("==================================================================")
    print(" 🌟 PART B: DEEPSEEK HARNESS & CREATOR MODE PLUGIN SUITE DEMO")
    print("==================================================================")
    
    engine = CreatorModeEngine()
    
    # 1. Creator Mode Prompt-to-Plugin Generation Demo
    print("\n--- 1. Creator Mode: Generate Plugin from Single Sentence ---")
    prompt = "Add a dinosaur jumping game floating in the bottom right"
    generated_plugin = engine.generate_plugin_from_prompt(prompt)
    print(f"✅ Generated & Hot-Loaded Plugin ID: {generated_plugin.plugin_id}")
    print(f"   Target UI Slot: {generated_plugin.ui_slot}")
    print(f"   Snippet Preview: {generated_plugin.code_snippet[:65]}...")
    
    # 2. Plugin 1 (Scratch): Second Brain / PKN
    print("\n--- 2. Plugin 1 (Scratch): Second Brain / PKN ---")
    pkn = SecondBrainPlugin()
    pkn.add_note("LLM Agent Benchmarks", "Evaluating harness performance with SWE-bench and HumanEval", ["benchmarks", "llm"])
    context_inj = pkn.inject_context("benchmarks")
    print("Injected Second Brain Context:\n", context_inj)
    
    # 3. Plugin 2 (Scratch): Dino Game Overlay
    print("--- 3. Plugin 2 (Scratch): Dino Game Floating Widget ---")
    dino = DinoGamePlugin()
    print("Rendered Widget HTML:\n", dino.render_html_widget()[:140], "...")
    
    # 4. Plugin 3: Cursor Debug Mode Preset
    print("\n--- 4. Plugin 3: Cursor Debug Mode Preset ---")
    debug_p = CursorDebugPlugin()
    res_debug = debug_p.execute_debug_protocol("server.py", "IndexError: list index out of range")
    print("Cursor Debug Execution Output:\n", json.dumps(res_debug, indent=2))
    
    # 5. Plugin 4: SEO Workbench
    print("\n--- 5. Plugin 4: SEO Workbench ---")
    seo = SEOWorkbenchPlugin()
    sample_html = "<html><head><title>DeepSeek Harness</title><meta name='description' content='Harness'></head><body><h1>Header</h1></body></html>"
    print("SEO Audit Result:\n", json.dumps(seo.audit_page("index.html", sample_html), indent=2))
    
    # 6. Plugin 5: Mirage VFS
    print("\n--- 6. Plugin 5: Mirage In-Memory VFS ---")
    mirage = MirageVFSPlugin()
    print(mirage.write_vfs("/vfs/test.txt", "Hello Mirage RAM VFS!"))
    print(mirage.exec_vfs_shell("python3 /vfs/test.txt"))
    
    # 7. Plugin 6: Autopilot Task Graph
    print("\n--- 7. Plugin 6: Autopilot Task Graph ---")
    autopilot = AutopilotPlugin()
    print(autopilot.pass_evidence_gate("t1", "Scaffold created with 0 errors"))
    print("Task Graph Status:\n", json.dumps(autopilot.get_graph_status()[:2], indent=2))
    
    # 8. Plugin 7: Team Plan Canvas
    print("\n--- 8. Plugin 7: Team Plan & Collaborative Canvas ---")
    team = TeamCanvasPlugin()
    print("Team Canvas Workflow Output:\n", json.dumps(team.run_team_workflow("Build Autonomous Agent Harness"), indent=2))
    
    # 9. Trajectory Stream & Forking Inspection
    print("\n--- 9. Event Stream Trajectory Inspection & Forking ---")
    print(f"Total Trajectory Events Captured: {len(engine.event_stream.events)}")
    forked = engine.event_stream.fork(engine.event_stream.events[0].id)
    print(f"Forked Stream ID: {forked.stream_id} with {len(forked.events)} events.")
    
    print("\n==================================================================")
    print(" 🎉 PART B DEEPSEEK HARNESS & 7 PLUGINS DEMO COMPLETED SUCCESSFULLY!")
    print("==================================================================")

if __name__ == "__main__":
    run_dsh_master_demo()

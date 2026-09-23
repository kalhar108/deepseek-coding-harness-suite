"""
PART A - STEP 4: Full Production Coding Harness CLI & API
Combines Minimal Agent Loop, Tool Harness, Context Window Manager, and Evaluation Harness.
Supports multi-provider configuration, rich color logs, and session snapshot telemetry.
"""

import os
import sys
import json
import time
from typing import Dict, Any, List, Optional
from part_a_harness.llm_client import UnifiedLLMClient
from part_a_harness.step2_tool_harness import ToolHarness, ContextWindowManager

class FullCodingHarness:
    """Production Coding Harness Engine orchestrating tools, context, telemetry, and execution."""
    def __init__(self, work_dir: str = ".", provider: str = "mock", model: str = "deepseek/deepseek-r1"):
        self.work_dir = os.path.abspath(work_dir)
        self.client = UnifiedLLMClient(provider=provider, model=model)
        self.tool_harness = ToolHarness(self.work_dir)
        self.context_mgr = ContextWindowManager(max_tokens=8000)
        self.session_history: List[Dict[str, Any]] = [
            {
                "role": "system",
                "content": (
                    "You are a state-of-the-art autonomous Coding Harness Agent. "
                    "You write clean, safe code, run unit tests, repair bugs, and apply file patches. "
                    "Always verify changes before marking a task complete."
                )
            }
        ]
        self.tools_schema = [
            {
                "type": "function",
                "function": {
                    "name": "read_file",
                    "description": "Read contents of a file with line numbers",
                    "parameters": {"type": "object", "properties": {"path": {"type": "string"}}}
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "write_file",
                    "description": "Write text content to a file",
                    "parameters": {"type": "object", "properties": {"path": {"type": "string"}, "content": {"type": "string"}}, "required": ["path", "content"]}
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "apply_patch",
                    "description": "Apply search and replace patch block to a file",
                    "parameters": {"type": "object", "properties": {"path": {"type": "string"}, "search_block": {"type": "string"}, "replace_block": {"type": "string"}}, "required": ["path", "search_block", "replace_block"]}
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "parse_ast",
                    "description": "Parse AST summary (classes & functions) of Python file",
                    "parameters": {"type": "object", "properties": {"path": {"type": "string"}}}
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "exec_sandbox",
                    "description": "Execute shell command inside sandboxed work directory",
                    "parameters": {"type": "object", "properties": {"command": {"type": "string"}}, "required": ["command"]}
                }
            }
        ]

    def _execute_tool_call(self, name: str, args: dict) -> str:
        if name == "read_file":
            return self.tool_harness.read_file(args.get("path", ""))
        elif name == "write_file":
            return self.tool_harness.write_file(args.get("path", ""), args.get("content", ""))
        elif name == "apply_patch":
            return self.tool_harness.apply_patch(args.get("path", ""), args.get("search_block", ""), args.get("replace_block", ""))
        elif name == "parse_ast":
            return self.tool_harness.parse_ast(args.get("path", ""))
        elif name in ["exec_sandbox", "exec_command"]:
            return self.tool_harness.exec_sandbox(args.get("command", ""))
        return f"Unknown tool invocation: {name}"

    def run_task(self, user_instruction: str, max_turns: int = 5) -> Dict[str, Any]:
        """Execute user prompt through the complete Harness control loop."""
        self.session_history.append({"role": "user", "content": user_instruction})
        print(f"\n==================================================================")
        print(f" 🚀 FULL HARNESS EXECUTION | Target: '{user_instruction[:70]}...'")
        print(f"==================================================================")
        
        telemetry = {"start_time": time.time(), "turns": 0, "tool_executions": []}

        for turn in range(max_turns):
            telemetry["turns"] += 1
            self.session_history = self.context_mgr.prune_context(self.session_history)
            
            print(f"\n⚡ Turn {turn+1}/{max_turns} | History Tokens: ~{self.context_mgr.estimate_tokens(self.session_history)}")
            response = self.client.chat_completion(self.session_history, self.tools_schema)
            self.session_history.append(response)

            tool_calls = response.get("tool_calls")
            if tool_calls:
                for call in tool_calls:
                    fn_name = call["function"]["name"]
                    fn_args = json.loads(call["function"]["arguments"]) if isinstance(call["function"]["arguments"], str) else call["function"]["arguments"]
                    print(f"   ⚙️  [Tool Call]: {fn_name}({fn_args})")
                    
                    output = self._execute_tool_call(fn_name, fn_args)
                    telemetry["tool_executions"].append({"tool": fn_name, "args": fn_args, "output_preview": output[:100]})
                    print(f"   📥 [Result]: {output.strip()[:120]}...")
                    
                    self.session_history.append({
                        "role": "tool",
                        "tool_call_id": call.get("id", "call_1"),
                        "content": output
                    })
            else:
                print(f"\n🎯 [Final Answer]:\n{response.get('content', '')}")
                break

        telemetry["total_duration"] = round(time.time() - telemetry["start_time"], 3)
        return {
            "status": "success",
            "telemetry": telemetry,
            "final_response": self.session_history[-1].get("content", "")
        }

if __name__ == "__main__":
    harness = FullCodingHarness(work_dir=".")
    result = harness.run_task("Audit current directory files and execute python test runner.")
    print("\nTelemetry Report:\n", json.dumps(result["telemetry"], indent=2))

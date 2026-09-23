"""
PART A - STEP 2: Advanced Tool Harness & Context Manager
Includes unified diff editing, AST parsing, token-window context management, and sandbox shell.
"""

import os
import ast
import json
import subprocess
from typing import List, Dict, Any, Optional
from part_a_harness.llm_client import UnifiedLLMClient

class ContextWindowManager:
    """Manages agent token budget and prunes old context when limits are reached."""
    def __init__(self, max_tokens: int = 8000):
        self.max_tokens = max_tokens

    def estimate_tokens(self, messages: List[Dict[str, Any]]) -> int:
        return sum(len(str(m.get("content", ""))) // 4 for m in messages)

    def prune_context(self, messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Keep system message + recent conversation turns."""
        if self.estimate_tokens(messages) <= self.max_tokens:
            return messages
        system_msg = [m for m in messages if m.get("role") == "system"]
        other_msgs = [m for m in messages if m.get("role") != "system"]
        trimmed = system_msg + other_msgs[-6:]
        print(f"[ContextWindowManager] Trimmed conversation history to fit {self.max_tokens} token budget.")
        return trimmed

class ToolHarness:
    """Comprehensive tool harness for file operations, AST parsing, diff patching, and shell sandbox."""
    def __init__(self, work_dir: str):
        self.work_dir = os.path.abspath(work_dir)

    def read_file(self, relative_path: str, start_line: Optional[int] = None, end_line: Optional[int] = None) -> str:
        path = os.path.join(self.work_dir, relative_path)
        if not os.path.exists(path):
            return f"Error: File '{relative_path}' does not exist."
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if start_line is not None and end_line is not None:
            selected = lines[max(0, start_line-1):end_line]
            return "".join([f"{i+start_line}: {line}" for i, line in enumerate(selected)])
        return "".join([f"{i+1}: {line}" for i, line in enumerate(lines)])

    def write_file(self, relative_path: str, content: str) -> str:
        path = os.path.join(self.work_dir, relative_path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully wrote {len(content)} characters to '{relative_path}'."

    def apply_patch(self, relative_path: str, search_block: str, replace_block: str) -> str:
        path = os.path.join(self.work_dir, relative_path)
        if not os.path.exists(path):
            return f"Error: File '{relative_path}' not found for patching."
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if search_block not in content:
            return f"Patch failed: Target block not found in '{relative_path}'."
        updated = content.replace(search_block, replace_block, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        return f"Patch successfully applied to '{relative_path}'."

    def parse_ast(self, relative_path: str) -> str:
        path = os.path.join(self.work_dir, relative_path)
        if not os.path.exists(path):
            return f"Error: File '{relative_path}' not found."
        try:
            with open(path, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())
            classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
            functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            return f"AST Summary for {relative_path}:\n  Classes: {classes}\n  Functions: {functions}"
        except Exception as e:
            return f"AST Parsing failed: {e}"

    def exec_sandbox(self, command: str, timeout: int = 10) -> str:
        try:
            res = subprocess.run(
                command,
                shell=True,
                cwd=self.work_dir,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            out = res.stdout.strip()
            err = res.stderr.strip()
            return f"[Exit Code {res.returncode}]\nStdout:\n{out}\nStderr:\n{err}"
        except subprocess.TimeoutExpired:
            return f"Execution timed out after {timeout} seconds."

def step2_demo():
    harness = ToolHarness(os.getcwd())
    context_mgr = ContextWindowManager(max_tokens=4000)
    
    print("=== STEP 2: Advanced Tool Harness Demo ===")
    test_filename = "temp_calculator.py"
    
    # 1. Write file
    code = "def add(a, b):\n    return a + b\n\ndef multiply(a, b):\n    return a * b\n"
    print("1. Writing file:", harness.write_file(test_filename, code))
    
    # 2. Parse AST
    print("2. Parsing AST:\n", harness.parse_ast(test_filename))
    
    # 3. Apply Patch
    patch_target = "def multiply(a, b):\n    return a * b"
    patch_replacement = "def multiply(a, b):\n    # Enhanced multiplication\n    return a * b"
    print("3. Applying Patch:", harness.apply_patch(test_filename, patch_target, patch_replacement))
    
    # 4. Read back with line numbers
    print("4. Reading File:\n", harness.read_file(test_filename))
    
    # 5. Exec Sandbox
    print("5. Running Sandbox Command:", harness.exec_sandbox(f"python3 {test_filename}"))
    
    # Cleanup
    if os.path.exists(test_filename):
        os.remove(test_filename)

if __name__ == "__main__":
    step2_demo()

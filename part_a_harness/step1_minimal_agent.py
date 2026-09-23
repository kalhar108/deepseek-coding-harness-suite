"""
PART A - STEP 1: Minimal Agent (~20-line core LLM tool call loop)
Inspired by Decoding AI & Mini-SWE-agent.
Demonstrates the foundational REPL loop: prompt -> call LLM -> parse tool -> execute -> loop back.
"""

import json
from part_a_harness.llm_client import UnifiedLLMClient

def execute_tool(name: str, args: dict) -> str:
    if name == "read_file":
        try:
            with open(args.get("path", ""), "r") as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"
    elif name == "exec_command":
        import subprocess
        res = subprocess.run(args.get("command", ""), shell=True, capture_output=True, text=True)
        return res.stdout or res.stderr
    return f"Unknown tool: {name}"

def minimal_agent_loop(user_prompt: str, max_turns: int = 5):
    client = UnifiedLLMClient()
    messages = [
        {"role": "system", "content": "You are a minimal coding agent. Use available tools to solve user tasks."},
        {"role": "user", "content": user_prompt}
    ]
    tools = [
        {"type": "function", "function": {"name": "read_file", "description": "Read file contents", "parameters": {"type": "object", "properties": {"path": {"type": "string"}}}}},
        {"type": "function", "function": {"name": "exec_command", "description": "Run shell command", "parameters": {"type": "object", "properties": {"command": {"type": "string"}}}}}
    ]

    print(f"=== STEP 1: Minimal Agent Loop initialized for prompt: '{user_prompt}' ===")
    for turn in range(max_turns):
        print(f"\n--- Turn {turn+1} ---")
        response = client.chat_completion(messages, tools)
        messages.append(response)
        
        if response.get("tool_calls"):
            for call in response["tool_calls"]:
                tool_name = call["function"]["name"]
                tool_args = json.loads(call["function"]["arguments"])
                print(f" Tool Call: {tool_name}({tool_args})")
                tool_output = execute_tool(tool_name, tool_args)
                print(f" Output: {tool_output.strip()[:100]}...")
                messages.append({"role": "tool", "tool_call_id": call["id"], "content": tool_output})
        else:
            print(f" Agent Final Output: {response['content']}")
            break

if __name__ == "__main__":
    minimal_agent_loop("Explore the directory and run python3 --version")

"""
PART A - STEP 3: Automated Evaluation Harness (SWE-bench / HumanEval style)
Evaluates code agent candidate patches against test suites and computes Pass@1 metrics.
"""

import os
import time
import json
import subprocess
from typing import Dict, Any, List
from part_a_harness.step2_tool_harness import ToolHarness

class BenchmarkProblem:
    def __init__(self, task_id: str, prompt: str, initial_code: str, test_script: str):
        self.task_id = task_id
        self.prompt = prompt
        self.initial_code = initial_code
        self.test_script = test_script

class EvaluationHarness:
    """Benchmark runner for automated agent code evaluation."""
    def __init__(self, work_dir: str):
        self.work_dir = work_dir
        self.tool_harness = ToolHarness(work_dir)

    def evaluate_task(self, problem: BenchmarkProblem, solution_code: str) -> Dict[str, Any]:
        """Run candidate solution against unit test suite."""
        solution_path = os.path.join(self.work_dir, f"solution_{problem.task_id}.py")
        test_path = os.path.join(self.work_dir, f"test_{problem.task_id}.py")
        
        # Write solution file and test runner file
        self.tool_harness.write_file(f"solution_{problem.task_id}.py", solution_code)
        self.tool_harness.write_file(f"test_{problem.task_id}.py", problem.test_script)
        
        start_time = time.time()
        result = self.tool_harness.exec_sandbox(f"python3 test_{problem.task_id}.py")
        duration = time.time() - start_time
        
        passed = "[Exit Code 0]" in result and "FAIL" not in result
        
        # Clean up temporary test files
        if os.path.exists(solution_path): os.remove(solution_path)
        if os.path.exists(test_path): os.remove(test_path)
        
        return {
            "task_id": problem.task_id,
            "passed": passed,
            "duration": round(duration, 3),
            "output": result
        }

    def run_benchmark_suite(self, problems: List[BenchmarkProblem], solutions: Dict[str, str]) -> Dict[str, Any]:
        """Evaluate a set of benchmark problems and calculate Pass@1."""
        results = []
        passed_count = 0
        
        for prob in problems:
            sol = solutions.get(prob.task_id, prob.initial_code)
            res = self.evaluate_task(prob, sol)
            results.append(res)
            if res["passed"]:
                passed_count += 1
                
        pass_at_1 = (passed_count / len(problems)) * 100 if problems else 0.0
        return {
            "total_problems": len(problems),
            "passed_problems": passed_count,
            "pass_at_1_accuracy": f"{pass_at_1:.1f}%",
            "detailed_results": results
        }

def step3_demo():
    eval_harness = EvaluationHarness(os.getcwd())
    
    # Define benchmark problems (HumanEval style)
    problems = [
        BenchmarkProblem(
            task_id="problem_1",
            prompt="Write a function is_palindrome(s: str) -> bool",
            initial_code="def is_palindrome(s: str) -> bool:\n    return s == s[::-1]",
            test_script="""import sys
from solution_problem_1 import is_palindrome

assert is_palindrome("radar") == True
assert is_palindrome("hello") == False
assert is_palindrome("racecar") == True
print("ALL TESTS PASSED")
"""
        ),
        BenchmarkProblem(
            task_id="problem_2",
            prompt="Write a function fibonacci(n: int) -> int",
            initial_code="def fibonacci(n: int) -> int:\n    if n <= 1: return n\n    return fibonacci(n-1) + fibonacci(n-2)",
            test_script="""import sys
from solution_problem_2 import fibonacci

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(5) == 5
assert fibonacci(7) == 13
print("ALL TESTS PASSED")
"""
        )
    ]

    solutions = {
        "problem_1": "def is_palindrome(s: str) -> bool:\n    clean = ''.join(c.lower() for c in s if c.isalnum())\n    return clean == clean[::-1]",
        "problem_2": "def fibonacci(n: int) -> int:\n    if n <= 1: return n\n    a, b = 0, 1\n    for _ in range(2, n + 1):\n        a, b = b, a + b\n    return b"
    }

    print("=== STEP 3: Automated Evaluation Harness Demo ===")
    summary = eval_harness.run_benchmark_suite(problems, solutions)
    print("Benchmark Suite Execution Summary:")
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    step3_demo()

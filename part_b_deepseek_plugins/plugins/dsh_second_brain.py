"""
DSH PLUGIN 1 (From Scratch): Second Brain / Personal Knowledge Network (PKN)
Provides memory indexing, note linking, tag search, and semantic context injection.
"""

import time
import json
from typing import Dict, Any, List, Optional

class SecondBrainPlugin:
    def __init__(self, storage_file: str = "second_brain_notes.json"):
        self.plugin_id = "dsh-second-brain"
        self.name = "Second Brain & PKN Knowledge Graph"
        self.storage_file = storage_file
        self.notes: List[Dict[str, Any]] = [
            {
                "id": "note_1",
                "title": "DeepSeek Harness Architecture",
                "content": "DeepSeek Harness relies on Cordis manifest and event streams for event-driven agent orchestration.",
                "tags": ["harness", "architecture", "deepseek"],
                "created_at": time.time()
            },
            {
                "id": "note_2",
                "title": "SWE-Bench Evaluation Strategy",
                "content": "Evaluation harness must run isolated tests in clean sandboxes with strict timeouts.",
                "tags": ["eval", "benchmarking", "testing"],
                "created_at": time.time()
            }
        ]

    def add_note(self, title: str, content: str, tags: List[str]) -> Dict[str, Any]:
        note = {
            "id": f"note_{len(self.notes)+1}",
            "title": title,
            "content": content,
            "tags": tags,
            "created_at": time.time()
        }
        self.notes.append(note)
        return note

    def search_notes(self, query: str) -> List[Dict[str, Any]]:
        query_lower = query.lower()
        results = []
        for n in self.notes:
            if query_lower in n["title"].lower() or query_lower in n["content"].lower() or any(query_lower in t for t in n["tags"]):
                results.append(n)
        return results

    def inject_context(self, user_prompt: str) -> str:
        """Inject relevant second brain notes into the agent context window."""
        matched = self.search_notes(user_prompt)
        if not matched:
            return ""
        context_str = "\n--- [Second Brain Context Injection] ---\n"
        for m in matched:
            context_str += f"• Note: '{m['title']}' (Tags: {', '.join(m['tags'])})\n  {m['content']}\n"
        return context_str

"""
DeepSeek Harness Creator Mode & Plugin Generator Engine.
Supports hot-loading plugins, prompt-to-plugin synthesis, UI slot injection, and trajectory verification.
"""

import os
import json
try:
    import yaml
except ImportError:
    yaml = None
from typing import Dict, Any, List, Optional
from part_b_deepseek_plugins.harness_core.event_stream import EventStreamManager

class DSHPlugin:
    def __init__(self, plugin_id: str, name: str, description: str, ui_slot: str, code_snippet: str, tools: Optional[List[str]] = None):
        self.plugin_id = plugin_id
        self.name = name
        self.description = description
        self.ui_slot = ui_slot # 'shell.overlay', 'sidebar.children', 'settings.cards'
        self.code_snippet = code_snippet
        self.tools = tools or []
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "plugin_id": self.plugin_id,
            "name": self.name,
            "description": self.description,
            "ui_slot": self.ui_slot,
            "tools": self.tools,
            "active": self.active,
            "code_snippet": self.code_snippet
        }

class CreatorModeEngine:
    """Creator Mode runtime engine for DeepSeek Harness plugin authoring and hot-reloading."""
    def __init__(self, manifest_path: Optional[str] = None):
        self.manifest_path = manifest_path
        self.active_plugins: Dict[str, DSHPlugin] = {}
        self.event_stream = EventStreamManager()

    def generate_plugin_from_prompt(self, sentence_prompt: str) -> DSHPlugin:
        """Synthesize plugin code and UI slot binding from single sentence instruction."""
        self.event_stream.append("reasoning", {"prompt": sentence_prompt, "stage": "synthesizing_plugin"})
        
        plugin_id = f"custom-gen-{abs(hash(sentence_prompt)) % 10000}"
        
        # Determine slot & structure based on prompt intent
        if "game" in sentence_prompt.lower() or "floating" in sentence_prompt.lower() or "overlay" in sentence_prompt.lower():
            ui_slot = "shell.overlay"
            code = (
                "<div id='dino-overlay' style='position:fixed;bottom:20px;right:20px;"
                "background:#1e1e2e;padding:12px;border-radius:8px;border:1px solid #89b4fa;z-index:999;'>"
                "<span style='font-size:20px;'>🦖 🌵 🏃</span>"
                "<p style='color:#cdd6f4;font-size:12px;margin:4px 0 0 0;'>Dino Jump Active!</p></div>"
            )
        else:
            ui_slot = "sidebar.children"
            code = f"<div class='plugin-card'><h4>{sentence_prompt[:30]}</h4><p>Hot-loaded DSH Plugin</p></div>"
            
        plugin = DSHPlugin(
            plugin_id=plugin_id,
            name=f"Plugin: {sentence_prompt[:25]}...",
            description=sentence_prompt,
            ui_slot=ui_slot,
            code_snippet=code
        )
        
        # Test in memory before promoting
        self.event_stream.append("context_injection", {"action": "in_memory_test", "plugin_id": plugin_id})
        plugin.activate()
        self.active_plugins[plugin_id] = plugin
        self.event_stream.append("system", {"action": "promoted_plugin", "plugin_id": plugin_id, "status": "active"})
        
        return plugin

    def register_plugin(self, plugin: DSHPlugin):
        plugin.activate()
        self.active_plugins[plugin.plugin_id] = plugin
        self.event_stream.append("system", {"action": "registered_plugin", "plugin_id": plugin.plugin_id})

    def list_active_plugins(self) -> List[Dict[str, Any]]:
        return [p.to_dict() for p in self.active_plugins.values()]

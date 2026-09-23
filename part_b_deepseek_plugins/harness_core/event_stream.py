"""
DeepSeek Harness Append-Only Event Stream Engine.
Manages trajectory tracking, run forking, event replay, and creator mode inspection.
"""

import time
import json
import uuid
from typing import Dict, Any, List, Optional

class TrajectoryEvent:
    def __init__(self, event_type: str, data: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None):
        self.id = str(uuid.uuid4())[:8]
        self.timestamp = time.time()
        self.type = event_type # 'system', 'reasoning', 'tool', 'subagent', 'context_injection'
        self.data = data
        self.metadata = metadata or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "type": self.type,
            "data": self.data,
            "metadata": self.metadata
        }

class EventStreamManager:
    def __init__(self, stream_id: Optional[str] = None):
        self.stream_id = stream_id or str(uuid.uuid4())[:8]
        self.events: List[TrajectoryEvent] = []

    def append(self, event_type: str, data: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> TrajectoryEvent:
        event = TrajectoryEvent(event_type, data, metadata)
        self.events.append(event)
        return event

    def fork(self, at_event_id: str) -> 'EventStreamManager':
        """Fork run trajectory from a specific event ID for Creator Mode testing."""
        forked_stream = EventStreamManager()
        for ev in self.events:
            forked_stream.events.append(ev)
            if ev.id == at_event_id:
                break
        print(f"[EventStream] Forked stream {self.stream_id} -> {forked_stream.stream_id} at event {at_event_id}")
        return forked_stream

    def replay(self) -> List[Dict[str, Any]]:
        """Replay trajectory events in chronological order."""
        return [ev.to_dict() for ev in self.events]

    def export_trajectory(self) -> str:
        return json.dumps({
            "stream_id": self.stream_id,
            "total_events": len(self.events),
            "trajectory": self.replay()
        }, indent=2)

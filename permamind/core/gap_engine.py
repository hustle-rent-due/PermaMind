import uuid
import time
from typing import Any, Optional

class GapEngine:
    def __init__(self, memory, sensitivity: float = 1.0):
        self.memory = memory
        self.k = float(sensitivity)

    def compute_gap(self, prediction: Any, outcome: Any) -> float:
        if prediction == outcome:
            return 0.0
        if isinstance(prediction, (int, float)) and isinstance(outcome, (int, float)):
            return abs(float(prediction) - float(outcome))
        return 1.0

    def record(self, context: str, prediction: Any, outcome: Any, action: Optional[str] = None):
        gap = self.compute_gap(prediction, outcome)
        priority = self.k * gap

        data = self.memory.load()
        data["events"].append({
            "id": str(uuid.uuid4()),
            "time": time.time(),
            "context": context,
            "prediction": prediction,
            "outcome": outcome,
            "gap": gap,
            "priority": priority,
            "action": action
        })
        self.memory.save(data)
        return gap, priority


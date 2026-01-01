import re

def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower().strip())

class ConfidenceGate:
    def __init__(self, memory, threshold: float = 0.3):
        self.memory = memory
        self.threshold = float(threshold)

    def allow_assertion(self, context: str) -> bool:
        ctx = _norm(context)
        events = self.memory.load().get("events", [])

        for e in events:
            if e["gap"] >= self.threshold and ctx in _norm(e["context"]):
                return False
        return True


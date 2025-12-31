class ConfidenceGate:
    def __init__(self, memory, threshold: float = 0.3):
        self.memory = memory
        self.threshold = threshold

    def allow_assertion(self, context: str) -> bool:
        events = self.memory.load().get("events", [])
        for e in events:
            if e["gap"] >= self.threshold and context.lower() in e["context"].lower():
                return False
        return True

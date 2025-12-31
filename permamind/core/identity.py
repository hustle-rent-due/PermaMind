class IdentityModel:
    def __init__(self, memory):
        self.memory = memory

    def summarize(self):
        data = self.memory.load()
        beliefs = data.get("beliefs", {})
        events = data.get("events", [])
        return {
            "total_experiences": len(events),
            "confidence_constraints": [
                e for e in events if e["gap"] > 0.7
            ][-3:]
        }

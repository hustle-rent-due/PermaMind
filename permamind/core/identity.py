class IdentityModel:
    def __init__(self, memory):
        self.memory = memory

    def summarize(self):
        data = self.memory.load()
        events = data.get("events", [])

        high_gap = [e for e in events if e["gap"] > 0.7][-3:]

        return {
            "schema_version": data.get("schema_version"),
            "total_experiences": len(events),
            "last_updated": data.get("updated_at"),
            "confidence_constraints": high_gap
        }

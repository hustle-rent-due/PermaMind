import uuid
import datetime as dt

class GapEngine:
    def __init__(self, memory, sensitivity: float = 1.0):
        self.memory = memory
        self.k = sensitivity

    def compute_gap(self, prediction, outcome) -> float:
        if prediction == outcome:
            return 0.0
        return abs(float(prediction) - float(outcome)) if all(
            isinstance(x, (int, float)) for x in [prediction, outcome]
        ) else 1.0

    def record(self, context, prediction, outcome, action=None):
        gap = self.compute_gap(prediction, outcome)
        priority = self.k * gap

        data = self.memory.load()
        data["events"].append({
            "id": str(uuid.uuid4()),
            "time": dt.datetime.utcnow().isoformat(),
            "context": context,
            "prediction": prediction,
            "outcome": outcome,
            "gap": gap,
            "priority": priority,
            "action": action
        })
        self.memory.save(data)
        return gap, priority

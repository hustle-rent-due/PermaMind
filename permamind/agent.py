from core.memory import IdentityMemory
from core.gap_engine import GapEngine
from core.confidence_gate import ConfidenceGate
from core.policy import DecisionPolicy
from core.identity import IdentityModel

class PermaMindAgent:
    def __init__(self, path="permamind.json"):
        self.memory = IdentityMemory(path)
        self.gap_engine = GapEngine(self.memory)
        self.confidence_gate = ConfidenceGate(self.memory)
        self.policy = DecisionPolicy()
        self.identity = IdentityModel(self.memory)

    def decide(self, context, options):
        if not self.confidence_gate.allow_assertion(context):
            return {"action": "IDK", "reason": "Unresolved historical failure"}
        return self.policy.choose(options)

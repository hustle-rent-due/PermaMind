from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class DecisionOutcome:
    context: str
    prediction: Any
    outcome: Any
    action: Optional[str]
    gap: float
    priority: float

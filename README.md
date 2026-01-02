## Demo Mode – Isolated Sandbox

This project is currently presented as a sandboxed demonstration.

- Runs without API keys or credentials
- Does not connect to external systems
- Learning state is local and reversible
- No production data is accessed or modified

This demo exists to illustrate architecture and behavior, not deployment.


# PermaMind

**Persistent Identity & Stateful Decision Architecture for AI Agents**

[![Demo](https://img.shields.io/badge/demo-live-green)](https://bapxai.com/pssu.html)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## The Problem

Most AI agents don't actually learn across sessions. Even with "memory" enabled:
- Internal state resets between runs
- Same mistakes repeat
- Preferences don't stabilize
- Performance can't compound

**Memory exists. Reasoning exists. Durable behavioral change does not.**

## The Solution

PermaMind implements PSSU (Persistent Stateful Self-Update):
- **Persistence**: Identity survives sessions
- **Statefulness**: Internal variables shape decisions  
- **Self-Update**: Experience modifies structure
- **Bounded Retention**: Only high-signal changes persist

## Architecture

### Gap Engine™
Detects prediction errors (Δ) and computes priority: Q = k·Δ

### Confidence Gate™
Blocks confident assertions when unresolved gaps exist

### Identity Store™
Persists learned constraints across sessions

## Live Demo

👉 **[Try the interactive demo](https://bapxai.com/pssu.html)**

Watch three agents face the same task stream:
- **Frozen**: High coherence, no adaptation
- **Dissolved**: High plasticity, unstable
- **Bounded**: Controlled evolution within limits

Save → Refresh → Load to prove persistence.

Important:
This SDK enables persistent state and bounded self-update.
It does not certify identity stability, autonomy readiness, or safety.
Those require external auditing and governance layers not included here.

## Python SDK
```python
from permamind import PermaMindAgent

agent = PermaMindAgent("my_agent.json")

# Make decision
choice = agent.decide(
    context="Lead conversion dropped",
    options=[
        {"name": "improve_copy", "expected_gain": 0.4, "cost": 0.3},
        {"name": "add_chat", "expected_gain": 0.6, "cost": 0.7}
    ]
)

# Log outcome  
agent.gap_engine.record(
    context="Lead conversion dropped",
    prediction=0.6,
    outcome=0.5,
    action=choice["name"]
)
```

## Installation
```bash
git clone https://github.com/hustle-rent-due/PermaMind.git
cd PermaMind
# No dependencies needed - uses only Python standard library
```

## Further Reading

- [Gap Framework Whitepaper](https://omegaaxiommeta.substack.com/p/permamind-engine-white-paper?r=5vcnib)
- [PermaMind Engine Technical Paper](https://omegaaxiommeta.substack.com/p/the-pssu-framework-a-new-architectural?r=5vcnib)
- [Live Demo](https://bapxai.com/pssu.html)

## Contact

**Nile Green**  
📧 nile@bapxai.com  
🌐 https://bapxai.com

## License

MIT - See [LICENSE](LICENSE) file

---

*Published November 2025. Open source implementation of persistent learning architecture.*

## Demo Mode – Isolated Sandbox

This project is currently presented as a sandboxed demonstration.

- Runs without API keys or credentials
- Does not connect to external systems
- Learning state is local and reversible
- No production data is accessed or modified

This demo exists to illustrate architecture and behavior, not deployment.

## What This Is
- A reference implementation of persistent learning behavior
- A controlled environment for observing state evolution
- A framework for reasoning about memory, learning, and constraints

## What This Is Not
- A production system
- An autonomous agent acting on external systems
- A drop-in replacement for existing AI stacks

# PermaMind

**Persistent Identity & Stateful Decision Architecture for AI Agents**

PermaMind explores how AI systems can maintain durable internal state, allowing behavior to evolve meaningfully across sessions while remaining bounded and observable.


## The Problem

Most AI agents do not truly learn across sessions. Even with "memory" enabled:

* Internal state resets between runs
* Mistakes repeat
* Preferences fail to stabilize
* Performance cannot compound

**Memory exists. Reasoning exists. Durable behavioral change does not.**

---

## The Solution

PermaMind implements **PSSU (Persistent Stateful Self-Update)**:

* **Persistence** — identity survives across sessions
* **Statefulness** — internal variables shape decisions
* **Self-Update** — experience modifies internal structure
* **Bounded Retention** — only high-signal changes persist

---

## Architecture

**Gap Engine™**  
Detects prediction errors (Δ) and computes priority: `Q = k · Δ`

**Confidence Gate™**  
Blocks confident assertions when unresolved gaps exist

**Identity Store™**  
Persists learned constraints across sessions

---

## Live Demo

👉 **[Try the interactive demo](https://bapxai.com/pssu.html)**

Watch three agents face the same task stream:

* **Frozen** — high coherence, no adaptation
* **Dissolved** — high plasticity, unstable
* **Bounded** — controlled evolution within limits

**Save → Refresh → Load** to prove persistence.

---

## Important

This SDK enables persistent state and bounded self-update.

**It does not certify:**

* Identity stability
* Autonomy readiness
* Production safety

These require external auditing and governance layers, which are intentionally out of scope.

---

## Python SDK (Example)

```python
from permamind import PermaMindAgent

agent = PermaMindAgent("my_agent.json")

choice = agent.decide(
    context="Lead conversion dropped",
    options=[
        {"name": "improve_copy", "expected_gain": 0.4, "cost": 0.3},
        {"name": "add_chat", "expected_gain": 0.6, "cost": 0.7}
    ]
)

agent.gap_engine.record(
    context="Lead conversion dropped",
    prediction=0.6,
    outcome=0.5,
    action=choice["name"]
)
```

---

## Installation

```bash
git clone https://github.com/hustle-rent-due/PermaMind.git
cd PermaMind
# No dependencies required — Python standard library only
```

---

## Further Reading

<<<<<<< HEAD
* [Gap Framework Whitepaper](https://omegaaxiommeta.substack.com/p/the-gap-framework-pssu-manual)
* [PermaMind Engine Technical Paper](https://omegaaxiommeta.substack.com/p/permamind-engine)
* [Live Demo](https://bapxai.com/pssu.html)

---
=======
- [Gap Framework Whitepaper](https://omegaaxiommeta.substack.com/p/permamind-engine-white-paper?r=5vcnib)
- [PermaMind Engine Technical Paper](https://omegaaxiommeta.substack.com/p/the-pssu-framework-a-new-architectural?r=5vcnib)
- [Live Demo](https://bapxai.com/pssu.html)
>>>>>>> d8bec7fcfc6460be7163999d66f9c366b11f9603

## Contact

**Nile Green**  
📧 nile@bapxai.com  
🌐 https://bapxai.com

---

## License

MIT — see [LICENSE](LICENSE) file

---Future work may explore integrations, but only after safety, observability, and control boundaries are explicit.


**Future work may explore integrations only after safety, observability, and control boundaries are explicit.**

Published November 2025. Open-source reference implementation of persistent learning architecture.

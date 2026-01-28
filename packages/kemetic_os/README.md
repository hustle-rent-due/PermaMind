# Kemetic OS (OSS Edition)

A small, symbolic, modular reference architecture for building agent *state loops*.

This repo packages six modules — **Ra**, **Thoth**, **Ma'at**, **Isis**, **Anubis**, **Osiris** — plus an orchestrator (**OSIRIS_OS**) that composes them into a repeatable cycle:

- **RA**: recursive awareness loop / observer step  
- **THOTH**: memory + event logging  
- **MA'AT**: balance / correction  
- **ANUBIS**: validation + filtering  
- **OSIRIS**: fragmentation + transformation  
- **ISIS**: compilation + “re-membering”  

> This is a *reference implementation* intended to be extended. Swap any module for your own.

## Install

```bash
pip install -e .
```

## Quick start

```bash
python -m kemetic_os.demo
```

Or in code:

```python
from kemetic_os import OSIRIS_OS

os = OSIRIS_OS(agent_id="demo-1", agent_name="Demo Agent")
os.boot()
for _ in range(3):
    out = os.process_cycle({"input": "hello"})
print(out)
```

## What’s included

- `kemetic_os/` — the package
- `kemetic_os/demo.py` — runnable demo
- `LICENSE` — MIT

## Contributing

PRs welcome. Keep changes small and include tests where possible.

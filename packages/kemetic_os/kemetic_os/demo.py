from __future__ import annotations

from .osiris_os import OSIRIS_OS

def main() -> None:
    os = OSIRIS_OS(agent_id="demo-1", agent_name="Demo Agent")
    boot = os.boot()
    print("Boot:", boot)
    for i in range(3):
        out = os.process_cycle({"cycle": i, "input": "hello"})
        st = out["state"]
        print(f"Cycle {i}:",
              "cycle_count=", st["cycle_count"],
              "awareness=", round(st["awareness_level"], 4),
              "balanced=", out["balanced"])

if __name__ == "__main__":
    main()

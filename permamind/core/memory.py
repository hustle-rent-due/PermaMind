import json
import os
from pathlib import Path
from typing import Dict, Any
import time

SCHEMA_VERSION = "v1"

class IdentityMemory:
    def __init__(self, path: str):
        self.path = Path(path)
        if not self.path.exists():
            self._init()

    def _init(self) -> None:
        data = {
            "schema_version": SCHEMA_VERSION,
            "created_at": time.time(),
            "updated_at": time.time(),
            "events": [],
            "beliefs": {},
            "identity": {}
        }
        self._atomic_write(data)

    def load(self) -> Dict[str, Any]:
        raw = json.loads(self.path.read_text(encoding="utf-8"))

        # forward compatibility
        raw.setdefault("schema_version", SCHEMA_VERSION)
        raw.setdefault("events", [])
        raw.setdefault("beliefs", {})
        raw.setdefault("identity", {})

        return raw

    def save(self, data: Dict[str, Any]) -> None:
        data["updated_at"] = time.time()
        self._atomic_write(data)

    def _atomic_write(self, obj: Dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        tmp.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
        os.replace(tmp, self.path)  # atomic

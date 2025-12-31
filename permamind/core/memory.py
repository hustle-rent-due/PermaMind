import json
from pathlib import Path

class IdentityMemory:
    def __init__(self, path: str):
        self.path = Path(path)
        if not self.path.exists():
            self._init()

    def _init(self):
        self.path.write_text(json.dumps({
            "events": [],
            "beliefs": {},
            "identity": {}
        }, indent=2))

    def load(self):
        return json.loads(self.path.read_text())

    def save(self, data):
        self.path.write_text(json.dumps(data, indent=2))

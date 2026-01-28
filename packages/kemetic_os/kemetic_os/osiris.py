"""OSIRIS — Transformation protocol.

This module provides a small, explicit transformation API used by OSIRIS_OS:
- fragment(state, num_pieces): deterministically slices a dict into fragments
- transform_with_delta(state, delta): applies a delta/patch and returns new state

The intent is to be simple, auditable, and easy to extend for your own agent.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import copy
import math


@dataclass
class OSIRIS:
    """State fragmentation + transformation helper."""

    agent_id: str

    def fragment(self, state: Dict[str, Any], num_pieces: int = 13) -> List[Dict[str, Any]]:
        """Split a state dict into up to `num_pieces` fragments.

        The algorithm preserves keys/values but distributes keys across fragments.
        If num_pieces > number of keys, some fragments will be empty.
        """
        if num_pieces <= 0:
            raise ValueError("num_pieces must be > 0")
        keys = list(state.keys())
        fragments: List[Dict[str, Any]] = [dict() for _ in range(num_pieces)]
        for idx, k in enumerate(keys):
            fragments[idx % num_pieces][k] = copy.deepcopy(state[k])
        return fragments

    def transform_with_delta(self, state: Dict[str, Any], delta: Dict[str, Any]) -> Dict[str, Any]:
        """Apply a learning delta to the state (non-destructive).

        Rules:
        - Primitive values overwrite existing values.
        - Dict values are merged recursively.
        - Lists are concatenated (unique-preserving for primitives) by default.
        """
        base = copy.deepcopy(state)

        def merge(a: Any, b: Any) -> Any:
            if isinstance(a, dict) and isinstance(b, dict):
                out = copy.deepcopy(a)
                for k, v in b.items():
                    out[k] = merge(out.get(k), v) if k in out else copy.deepcopy(v)
                return out
            if isinstance(a, list) and isinstance(b, list):
                out = copy.deepcopy(a)
                for item in b:
                    if item not in out:
                        out.append(copy.deepcopy(item))
                return out
            return copy.deepcopy(b)

        return merge(base, delta)

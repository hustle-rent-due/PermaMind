from core.agent import PermaMindAgent

def test_persistence(tmp_path):
    p = tmp_path / "agent.json"
    a1 = PermaMindAgent(str(p))
    a1.gap_engine.record("lead drop", 0.6, 0.2)

    a2 = PermaMindAgent(str(p))
    summary = a2.identity.summarize()
    assert summary["total_experiences"] == 1

def test_confidence_gate_blocks(tmp_path):
    p = tmp_path / "agent.json"
    a = PermaMindAgent(str(p))
    a.gap_engine.record("conversion dropped", 0.9, 0.1)

    assert not a.confidence_gate.allow_assertion("conversion dropped")

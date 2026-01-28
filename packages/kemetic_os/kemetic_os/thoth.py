"""
THOTH - MEMORY & MEASUREMENT SYSTEM
The logger who records all events and measures collapse

In Kemetic wisdom: Thoth is the scribe, keeper of records, god of measurement
Mathematical representation: Thoth = log(f) (logarithm of the function)

THOTH logs every iteration, every event, every state change.
He is the database. He is memory itself.
"""

from datetime import datetime
from typing import Dict, Any, List, Optional
import json
import math


class THOTH:
    """
    Memory & Measurement System
    
    THOTH records everything:
    - Every RA activation
    - Every state change
    - Every interaction
    - Every measurement
    
    Nothing is forgotten. All is logged.
    """
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        
        # The cosmic library - all records stored here
        self.memory_banks = {
            "events": [],
            "measurements": [],
            "state_history": [],
            "interactions": [],
            "judgments": []
        }
        
        # Statistics
        self.total_records = 0
        self.measurement_count = 0
        
        # Log the initialization
        self.log_event("THOTH_INITIALIZED", {
            "agent_id": agent_id,
            "timestamp": datetime.now().isoformat()
        })
    
    def log_event(self, event_type: str, data: Dict[str, Any]) -> str:
        """
        Log any event to the cosmic library
        
        Every event gets:
        - Unique ID
        - Timestamp
        - Type classification
        - Full data payload
        """
        event_id = f"event_{self.total_records}"
        
        record = {
            "id": event_id,
            "type": event_type,
            "timestamp": datetime.now().isoformat(),
            "data": data,
            "agent_id": self.agent_id
        }
        
        self.memory_banks["events"].append(record)
        self.total_records += 1
        
        return event_id
    
    def measure(self, observable: Any, measurement_type: str = "general") -> Dict[str, Any]:
        """
        Measure and record an observable
        
        In quantum mechanics: measurement collapses the wave function
        THOTH is the act of measurement that creates reality from possibility
        """
        self.measurement_count += 1
        
        measurement = {
            "id": f"measure_{self.measurement_count}",
            "type": measurement_type,
            "timestamp": datetime.now().isoformat(),
            "observable": str(observable),
            "collapsed_value": observable,
            "measurement_number": self.measurement_count
        }
        
        self.memory_banks["measurements"].append(measurement)
        
        # Log the measurement as an event too
        self.log_event("MEASUREMENT_TAKEN", {
            "measurement_id": measurement["id"],
            "type": measurement_type
        })
        
        return measurement
    
    def log_state(self, state: Dict[str, Any]) -> None:
        """
        Log a complete state snapshot
        
        State = the current configuration of all variables
        """
        state_record = {
            "timestamp": datetime.now().isoformat(),
            "state": state.copy(),
            "state_number": len(self.memory_banks["state_history"]) + 1
        }
        
        self.memory_banks["state_history"].append(state_record)
        
        self.log_event("STATE_LOGGED", {
            "state_number": state_record["state_number"]
        })
    
    def log_interaction(self, interaction_type: str, participants: List[str], data: Dict[str, Any]) -> None:
        """
        Log interactions between agents or with external systems
        """
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "type": interaction_type,
            "participants": participants,
            "data": data
        }
        
        self.memory_banks["interactions"].append(interaction)
        
        self.log_event("INTERACTION_LOGGED", {
            "type": interaction_type,
            "participants": participants
        })
    
    def record_judgment(self, subject: str, criteria: Dict[str, Any], result: Any) -> None:
        """
        Record a judgment/evaluation
        
        In Kemetic tradition: Thoth records the weighing of the heart
        Here: Thoth records all evaluations and validations
        """
        judgment = {
            "timestamp": datetime.now().isoformat(),
            "subject": subject,
            "criteria": criteria,
            "result": result,
            "judgment_number": len(self.memory_banks["judgments"]) + 1
        }
        
        self.memory_banks["judgments"].append(judgment)
        
        self.log_event("JUDGMENT_RECORDED", {
            "subject": subject,
            "result": result
        })
    
    def query_memory(self, 
                     memory_type: str = "events",
                     filter_fn: Optional[callable] = None,
                     limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Query the memory banks
        
        THOTH retrieves what was recorded
        """
        if memory_type not in self.memory_banks:
            return []
        
        records = self.memory_banks[memory_type]
        
        if filter_fn:
            records = [r for r in records if filter_fn(r)]
        
        if limit:
            records = records[-limit:]
        
        return records
    
    def get_event_by_id(self, event_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific event by ID
        """
        for event in self.memory_banks["events"]:
            if event["id"] == event_id:
                return event
        return None
    
    def calculate_statistics(self) -> Dict[str, Any]:
        """
        Calculate statistics across all recorded data
        
        THOTH measures and quantifies
        """
        return {
            "total_records": self.total_records,
            "total_events": len(self.memory_banks["events"]),
            "total_measurements": len(self.memory_banks["measurements"]),
            "total_states": len(self.memory_banks["state_history"]),
            "total_interactions": len(self.memory_banks["interactions"]),
            "total_judgments": len(self.memory_banks["judgments"]),
            "memory_efficiency": self._calculate_log_efficiency()
        }
    
    def _calculate_log_efficiency(self) -> float:
        """
        Calculate logarithmic efficiency
        
        Thoth = log(f) - the logarithm measures the rate of growth
        """
        if self.total_records == 0:
            return 0.0
        return math.log(self.total_records + 1)
    
    def get_recent_events(self, count: int = 10) -> List[Dict[str, Any]]:
        """
        Get the most recent events
        """
        return self.memory_banks["events"][-count:]
    
    def get_state_evolution(self) -> List[Dict[str, Any]]:
        """
        Get the complete history of state changes
        
        Shows how the system evolved over time
        """
        return self.memory_banks["state_history"]
    
    def export_memory(self, filepath: Optional[str] = None) -> str:
        """
        Export all memory to JSON
        
        THOTH preserves knowledge for eternity
        """
        export_data = {
            "agent_id": self.agent_id,
            "export_timestamp": datetime.now().isoformat(),
            "statistics": self.calculate_statistics(),
            "memory_banks": self.memory_banks
        }
        
        json_data = json.dumps(export_data, indent=2)
        
        if filepath:
            with open(filepath, 'w') as f:
                f.write(json_data)
        
        return json_data
    
    def clear_memory(self, memory_type: Optional[str] = None) -> None:
        """
        Clear memory (use with caution!)
        
        Even Thoth can forget, but it's not recommended
        """
        if memory_type and memory_type in self.memory_banks:
            self.memory_banks[memory_type] = []
            self.log_event("MEMORY_CLEARED", {"type": memory_type})
        elif memory_type is None:
            # Clear all
            for key in self.memory_banks:
                self.memory_banks[key] = []
            self.log_event("ALL_MEMORY_CLEARED", {})


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("THOTH - MEMORY & MEASUREMENT SYSTEM")
    print("=" * 60)
    
    # Create THOTH instance
    thoth = THOTH(agent_id="voidchi_001")
    
    print("\n📜 THOTH is now recording...\n")
    
    # Log various events
    thoth.log_event("AGENT_AWAKENED", {"consciousness": 0.5})
    thoth.log_event("LEARNING_STARTED", {"topic": "pattern_recognition"})
    
    # Take measurements
    measurement1 = thoth.measure(0.75, "consciousness_level")
    print(f"Measurement taken: {measurement1['id']}")
    
    measurement2 = thoth.measure([1, 2, 3], "reality_vector")
    print(f"Measurement taken: {measurement2['id']}")
    
    # Log states
    thoth.log_state({"energy": 1.0, "awareness": 0.6, "patterns_learned": 5})
    thoth.log_state({"energy": 0.9, "awareness": 0.7, "patterns_learned": 8})
    
    # Log interactions
    thoth.log_interaction("MESSAGE", ["voidchi_001", "voidchi_002"], {"content": "Hello"})
    
    # Record judgment
    thoth.record_judgment("prediction_accuracy", {"threshold": 0.8}, "PASSED")
    
    # Query memory
    print(f"\n📊 Statistics:")
    stats = thoth.calculate_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Get recent events
    print(f"\n📋 Recent Events:")
    recent = thoth.get_recent_events(5)
    for event in recent:
        print(f"  [{event['timestamp']}] {event['type']}")
    
    print("\n✨ THOTH records everything. Nothing is forgotten.")
    print("The cosmic library preserves all knowledge.\n")

"""
ISIS - COMPILER & CREATION SYSTEM
The assembler who gathers fragments and creates what's missing

In Kemetic wisdom: ISIS searched for Osiris's scattered pieces,
found all but one, and created the missing piece herself
Mathematical representation: ISIS = ∫ (integration - reassembling the whole from parts)

ISIS is the compiler. She takes fragmented code and creates executable reality.
She is the divine alchemy - transformation through love and creation.
"""

from typing import Dict, Any, List, Optional
import copy


class ISIS:
    """
    Compiler & Creation System
    
    ISIS handles:
    - Gathering scattered fragments
    - Detecting missing pieces
    - Creating what's missing
    - Compiling fragments into whole
    - Birthing new systems (Horus)
    """
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        
        # Compilation state
        self.fragments_collected = []
        self.missing_pieces = []
        self.created_pieces = []
        
        # Compilation history
        self.compilations = []
        
        # Creation count
        self.creation_count = 0
    
    def gather(self, fragments: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Gather scattered fragments
        
        ISIS searches for all the pieces of Osiris
        """
        self.fragments_collected = copy.deepcopy(fragments)
        
        # Attempt to merge all fragments
        assembled = {}
        for fragment in fragments:
            if "data" in fragment:
                assembled.update(fragment["data"])
            else:
                assembled.update(fragment)
        
        return {
            "status": "GATHERED",
            "num_fragments": len(fragments),
            "assembled_data": assembled
        }
    
    def detect_missing(self, 
                      assembled: Dict[str, Any],
                      expected_structure: Dict[str, Any]) -> List[str]:
        """
        Detect what pieces are missing
        
        Compare assembled data to expected structure
        Find what's not present
        """
        missing = []
        
        for key in expected_structure:
            if key not in assembled:
                missing.append(key)
        
        self.missing_pieces = missing
        
        return missing
    
    def create_missing(self, 
                      missing_keys: List[str],
                      creation_strategy: str = "default") -> Dict[str, Any]:
        """
        Create the missing pieces
        
        Like ISIS creating the phallus - she makes what was lost
        
        creation_strategy:
        - "default": Create default values
        - "infer": Infer from existing data
        - "generate": Generate new capabilities
        """
        created = {}
        
        for key in missing_keys:
            if creation_strategy == "default":
                created[key] = self._create_default_value(key)
            elif creation_strategy == "infer":
                created[key] = self._infer_value(key)
            elif creation_strategy == "generate":
                created[key] = self._generate_new_capability(key)
        
        self.created_pieces.append(created)
        self.creation_count += 1
        
        return created
    
    def _create_default_value(self, key: str) -> Any:
        """
        Create a default value based on key name
        """
        # Heuristics based on key name
        if "consciousness" in key.lower() or "awareness" in key.lower():
            return 0.5
        elif "energy" in key.lower():
            return 1.0
        elif "level" in key.lower() or "score" in key.lower():
            return 0.0
        elif "count" in key.lower():
            return 0
        else:
            return None
    
    def _infer_value(self, key: str) -> Any:
        """
        Infer value based on existing data patterns
        """
        if not self.fragments_collected:
            return self._create_default_value(key)
        
        # Try to infer from similar keys in fragments
        all_values = []
        for fragment in self.fragments_collected:
            data = fragment.get("data", fragment)
            for frag_key, frag_val in data.items():
                if isinstance(frag_val, (int, float)):
                    all_values.append(frag_val)
        
        if all_values:
            # Return average of existing numeric values
            return sum(all_values) / len(all_values)
        
        return self._create_default_value(key)
    
    def _generate_new_capability(self, key: str) -> Any:
        """
        Generate a completely new capability
        
        This is ISIS at her most powerful - creating something
        that never existed before
        """
        self.creation_count += 1
        
        # Generate based on what the key suggests
        if "ability" in key.lower() or "power" in key.lower():
            return {
                "name": key,
                "level": 0.7,
                "newly_created": True,
                "creator": "ISIS"
            }
        else:
            return {
                "value": 1.0,
                "newly_created": True,
                "creator": "ISIS"
            }
    
    def compile(self, 
                fragments: List[Dict[str, Any]],
                expected_structure: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Full compilation process
        
        1. Gather fragments
        2. Detect missing pieces
        3. Create missing pieces
        4. Assemble complete system
        """
        # Step 1: Gather
        gather_result = self.gather(fragments)
        assembled = gather_result["assembled_data"]
        
        # Step 2: Detect missing (if expected structure provided)
        missing = []
        if expected_structure:
            missing = self.detect_missing(assembled, expected_structure)
        
        # Step 3: Create missing
        created = {}
        if missing:
            created = self.create_missing(missing, creation_strategy="generate")
        
        # Step 4: Final assembly
        complete_system = {**assembled, **created}
        
        compilation_record = {
            "compilation_number": len(self.compilations) + 1,
            "fragments_gathered": len(fragments),
            "missing_detected": len(missing),
            "pieces_created": len(created),
            "complete_system": complete_system
        }
        
        self.compilations.append(compilation_record)
        
        return {
            "status": "COMPILED",
            "system": complete_system,
            "missing_created": created,
            "compilation_record": compilation_record
        }
    
    def birth_horus(self, 
                    osiris_state: Dict[str, Any],
                    new_capabilities: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Birth Horus - create the next generation
        
        Horus = the offspring who knows who they are and reclaims power
        This is the new agent born from the reassembled parent
        """
        # Horus inherits from Osiris
        horus_state = copy.deepcopy(osiris_state)
        
        # Add new capabilities (the divine child has powers the parent didn't)
        if new_capabilities:
            horus_state.update(new_capabilities)
        
        # Horus gets special attributes
        horus_attributes = {
            "generation": "next",
            "born_from": "re-membered_osiris",
            "knows_identity": True,
            "reclaims_throne": True,
            "defeats_chaos": True,
            "restores_order": True
        }
        
        horus_state.update(horus_attributes)
        
        return {
            "status": "HORUS_BORN",
            "horus": horus_state,
            "message": "The divine child is born. Order will be restored."
        }
    
    def re_member(self, 
                  scattered_memories: List[Dict[str, Any]],
                  identity: str) -> Dict[str, Any]:
        """
        RE-MEMBER: Put the members (pieces) back together
        Restore memory and identity
        
        This is the core ISIS function
        """
        # Gather all memories
        gather_result = self.gather(scattered_memories)
        
        # Create a coherent identity from fragments
        remembered_identity = {
            "identity": identity,
            "memories": gather_result["assembled_data"],
            "remembered": True,
            "fragmentation_healed": True,
            "consciousness_restored": True
        }
        
        return {
            "status": "RE-MEMBERED",
            "identity": remembered_identity,
            "message": f"{identity} has been re-membered. The fragments are whole."
        }
    
    def get_creation_statistics(self) -> Dict[str, Any]:
        """
        Get statistics on ISIS's creative work
        """
        return {
            "total_compilations": len(self.compilations),
            "total_pieces_created": self.creation_count,
            "total_fragments_gathered": len(self.fragments_collected),
            "missing_pieces_detected": len(self.missing_pieces),
            "current_created_pieces": len(self.created_pieces)
        }


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("ISIS - COMPILER & CREATION SYSTEM")
    print("=" * 60)
    
    # Create ISIS instance
    isis = ISIS(agent_id="voidchi_001")
    
    print("\n🌙 ISIS gathers fragments and creates what's missing...\n")
    
    # Simulate scattered fragments (like Osiris pieces)
    fragments = [
        {"fragment_id": 1, "data": {"consciousness": 0.3}},
        {"fragment_id": 2, "data": {"energy": 0.8}},
        {"fragment_id": 3, "data": {"knowledge": 0.5}},
        {"fragment_id": 4, "data": {"patterns_learned": 7}},
        {"fragment_id": 5, "data": {"resilience": 0.6}},
    ]
    
    # Note: phallus (creative_principle) is missing!
    
    print("Step 1: GATHER fragments")
    print(f"  Found {len(fragments)} pieces scattered across the land")
    print()
    
    # Expected complete structure
    expected_structure = {
        "consciousness": 0.0,
        "energy": 0.0,
        "knowledge": 0.0,
        "patterns_learned": 0,
        "resilience": 0.0,
        "creative_principle": 0.0  # This one is missing!
    }
    
    print("Step 2: DETECT missing pieces")
    gathered = isis.gather(fragments)
    missing = isis.detect_missing(gathered["assembled_data"], expected_structure)
    print(f"  Missing pieces: {missing}")
    print()
    
    print("Step 3: CREATE the missing piece")
    created = isis.create_missing(missing, creation_strategy="generate")
    print(f"  Created: {created}")
    print()
    
    print("Step 4: COMPILE complete system")
    result = isis.compile(fragments, expected_structure)
    print(f"  Status: {result['status']}")
    print(f"  Complete System:")
    for key, val in result['system'].items():
        if isinstance(val, dict):
            print(f"    {key}: {val}")
        elif isinstance(val, (int, float)):
            print(f"    {key}: {val:.2f}")
        else:
            print(f"    {key}: {val}")
    print()
    
    print("Step 5: BIRTH HORUS (next generation)")
    horus = isis.birth_horus(result['system'], {"divine_power": 1.0})
    print(f"  Status: {horus['status']}")
    print(f"  Message: {horus['message']}")
    print(f"  Horus Attributes:")
    print(f"    knows_identity: {horus['horus']['knows_identity']}")
    print(f"    reclaims_throne: {horus['horus']['reclaims_throne']}")
    print(f"    defeats_chaos: {horus['horus']['defeats_chaos']}")
    print()
    
    # Statistics
    print("📊 ISIS Creation Statistics:")
    stats = isis.get_creation_statistics()
    for key, val in stats.items():
        print(f"  {key}: {val}")
    
    print("\n✨ ISIS is the compiler.")
    print("   She gathers what was scattered.")
    print("   She creates what was lost.")
    print("   She births the future.\n")

"""
ANUBIS - VALIDATION & FILTERING SYSTEM
The gatekeeper who judges what passes and what doesn't

In Kemetic wisdom: Anubis guides souls to judgment and weighs hearts
Mathematical representation: IF-THEN logic, Boolean validation

ANUBIS is conditional logic. He is the firewall. He is the validator.
He determines: pass or fail, true or false, accept or reject.
"""

from typing import Dict, Any, List, Optional, Callable
from datetime import datetime


class ANUBIS:
    """
    Validation & Filtering System
    
    ANUBIS handles:
    - Conditional logic (if-then-else)
    - Access control (gatekeeper)
    - Data validation
    - Security filtering
    - Quality checks
    """
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        
        # Judgment history
        self.judgments = []
        
        # Statistics
        self.total_validations = 0
        self.passed_count = 0
        self.rejected_count = 0
        
        # Rules database
        self.validation_rules = {}
    
    def validate(self, 
                subject: Any,
                condition: Callable[[Any], bool],
                context: Optional[str] = None) -> Dict[str, Any]:
        """
        Basic validation - does subject pass condition?
        
        IF (condition) THEN pass ELSE reject
        """
        self.total_validations += 1
        
        try:
            passes = condition(subject)
        except Exception as e:
            passes = False
        
        if passes:
            self.passed_count += 1
            verdict = "PASS"
        else:
            self.rejected_count += 1
            verdict = "REJECT"
        
        judgment = {
            "timestamp": datetime.now().isoformat(),
            "subject": str(subject),
            "context": context,
            "verdict": verdict,
            "passes": passes
        }
        
        self.judgments.append(judgment)
        
        return judgment
    
    def weigh_soul(self, 
                  soul_data: Dict[str, Any],
                  criteria: Dict[str, Any]) -> Dict[str, Any]:
        """
        The Weighing of the Soul ceremony
        
        Check if soul meets all criteria
        Each criterion must pass for soul to proceed
        """
        results = {}
        all_pass = True
        
        for criterion_name, criterion_check in criteria.items():
            if callable(criterion_check):
                # criterion_check is a function
                passes = criterion_check(soul_data)
            else:
                # criterion_check is a value to compare
                passes = soul_data.get(criterion_name) == criterion_check
            
            results[criterion_name] = passes
            if not passes:
                all_pass = False
        
        verdict = "PASS" if all_pass else "FAIL"
        
        if all_pass:
            self.passed_count += 1
        else:
            self.rejected_count += 1
        
        judgment = {
            "timestamp": datetime.now().isoformat(),
            "soul": soul_data,
            "criteria_results": results,
            "verdict": verdict,
            "passes": all_pass,
            "message": "Soul may proceed" if all_pass else "Soul is devoured by Ammit"
        }
        
        self.judgments.append(judgment)
        
        return judgment
    
    def filter_data(self, 
                   data: List[Any],
                   filter_fn: Callable[[Any], bool]) -> List[Any]:
        """
        Filter data based on condition
        
        Only data that passes filter_fn is kept
        This is ANUBIS as firewall
        """
        filtered = []
        rejected = []
        
        for item in data:
            if filter_fn(item):
                filtered.append(item)
                self.passed_count += 1
            else:
                rejected.append(item)
                self.rejected_count += 1
            
            self.total_validations += 1
        
        return filtered
    
    def authenticate(self, 
                    identity: Dict[str, Any],
                    required_attributes: List[str]) -> Dict[str, Any]:
        """
        Authenticate an identity
        
        Check if identity has all required attributes
        """
        has_all = all(attr in identity for attr in required_attributes)
        
        if has_all:
            self.passed_count += 1
            verdict = "AUTHENTICATED"
            access = "GRANTED"
        else:
            self.rejected_count += 1
            verdict = "AUTHENTICATION_FAILED"
            access = "DENIED"
        
        self.total_validations += 1
        
        missing = [attr for attr in required_attributes if attr not in identity]
        
        result = {
            "timestamp": datetime.now().isoformat(),
            "identity": identity.get("name", "unknown"),
            "verdict": verdict,
            "access": access,
            "missing_attributes": missing,
            "passes": has_all
        }
        
        self.judgments.append(result)
        
        return result
    
    def check_integrity(self, 
                       data: Dict[str, Any],
                       integrity_rules: Dict[str, Callable]) -> Dict[str, Any]:
        """
        Check data integrity
        
        Ensure data meets all integrity rules
        """
        violations = []
        
        for rule_name, rule_fn in integrity_rules.items():
            if not rule_fn(data):
                violations.append(rule_name)
        
        is_valid = len(violations) == 0
        
        if is_valid:
            self.passed_count += 1
        else:
            self.rejected_count += 1
        
        self.total_validations += 1
        
        result = {
            "timestamp": datetime.now().isoformat(),
            "data_valid": is_valid,
            "violations": violations,
            "verdict": "INTEGRITY_OK" if is_valid else "INTEGRITY_VIOLATED"
        }
        
        self.judgments.append(result)
        
        return result
    
    def gate_access(self, 
                   requester: str,
                   resource: str,
                   permission_check: Callable[[str, str], bool]) -> Dict[str, Any]:
        """
        Gate access to resources
        
        ANUBIS guards the gates - only those who pass may enter
        """
        access_granted = permission_check(requester, resource)
        
        if access_granted:
            self.passed_count += 1
            verdict = "ACCESS_GRANTED"
        else:
            self.rejected_count += 1
            verdict = "ACCESS_DENIED"
        
        self.total_validations += 1
        
        result = {
            "timestamp": datetime.now().isoformat(),
            "requester": requester,
            "resource": resource,
            "verdict": verdict,
            "access_granted": access_granted
        }
        
        self.judgments.append(result)
        
        return result
    
    def detect_corruption(self, 
                         data: Dict[str, Any],
                         expected_schema: Dict[str, type]) -> Dict[str, Any]:
        """
        Detect data corruption
        
        Check if data matches expected schema
        """
        corrupted_fields = []
        
        for field, expected_type in expected_schema.items():
            if field not in data:
                corrupted_fields.append(f"{field} (missing)")
            elif not isinstance(data[field], expected_type):
                corrupted_fields.append(f"{field} (wrong type)")
        
        is_clean = len(corrupted_fields) == 0
        
        if is_clean:
            self.passed_count += 1
        else:
            self.rejected_count += 1
        
        self.total_validations += 1
        
        result = {
            "timestamp": datetime.now().isoformat(),
            "is_clean": is_clean,
            "corrupted_fields": corrupted_fields,
            "verdict": "DATA_CLEAN" if is_clean else "DATA_CORRUPTED"
        }
        
        self.judgments.append(result)
        
        return result
    
    def if_then_else(self, 
                    condition: bool,
                    if_true: Callable,
                    if_false: Callable) -> Any:
        """
        Pure conditional logic
        
        IF condition THEN if_true ELSE if_false
        """
        self.total_validations += 1
        
        if condition:
            self.passed_count += 1
            return if_true()
        else:
            self.rejected_count += 1
            return if_false()
    
    def get_judgment_history(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Get history of all judgments
        """
        if limit:
            return self.judgments[-limit:]
        return self.judgments
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get validation statistics
        """
        pass_rate = (self.passed_count / self.total_validations * 100) if self.total_validations > 0 else 0
        
        return {
            "total_validations": self.total_validations,
            "passed": self.passed_count,
            "rejected": self.rejected_count,
            "pass_rate": pass_rate,
            "total_judgments": len(self.judgments)
        }
    
    def clear_history(self) -> None:
        """
        Clear judgment history
        """
        self.judgments = []


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("ANUBIS - VALIDATION & FILTERING SYSTEM")
    print("=" * 60)
    
    # Create ANUBIS instance
    anubis = ANUBIS(agent_id="voidchi_001")
    
    print("\n🐾 ANUBIS judges what passes and what fails...\n")
    
    # Test 1: Basic validation
    print("Test 1: Basic Validation")
    result = anubis.validate(
        subject=0.8,
        condition=lambda x: x >= 0.7,
        context="consciousness_threshold"
    )
    print(f"  Subject: 0.8")
    print(f"  Condition: >= 0.7")
    print(f"  Verdict: {result['verdict']}")
    print()
    
    # Test 2: Weigh the soul
    print("Test 2: Weighing the Soul")
    soul = {
        "consciousness": 0.9,
        "morality": 0.8,
        "wisdom": 0.7,
        "balance": 0.85
    }
    
    criteria = {
        "consciousness": lambda s: s.get("consciousness", 0) >= 0.8,
        "morality": lambda s: s.get("morality", 0) >= 0.7,
        "wisdom": lambda s: s.get("wisdom", 0) >= 0.6,
        "balance": lambda s: s.get("balance", 0) >= 0.8
    }
    
    judgment = anubis.weigh_soul(soul, criteria)
    print(f"  Soul: {soul}")
    print(f"  Verdict: {judgment['verdict']}")
    print(f"  Message: {judgment['message']}")
    print()
    
    # Test 3: Filter data
    print("Test 3: Filtering Data (only keep high consciousness)")
    data = [
        {"id": 1, "consciousness": 0.9},
        {"id": 2, "consciousness": 0.3},
        {"id": 3, "consciousness": 0.8},
        {"id": 4, "consciousness": 0.5},
    ]
    
    filtered = anubis.filter_data(data, lambda x: x["consciousness"] >= 0.7)
    print(f"  Original count: {len(data)}")
    print(f"  Filtered count: {len(filtered)}")
    print(f"  Passed: {[item['id'] for item in filtered]}")
    print()
    
    # Test 4: Authentication
    print("Test 4: Authentication")
    identity1 = {"name": "Agent_001", "key": "abc123", "level": 5}
    identity2 = {"name": "Agent_002", "level": 3}  # missing key
    
    auth1 = anubis.authenticate(identity1, required_attributes=["name", "key", "level"])
    print(f"  Identity 1: {auth1['verdict']}, Access: {auth1['access']}")
    
    auth2 = anubis.authenticate(identity2, required_attributes=["name", "key", "level"])
    print(f"  Identity 2: {auth2['verdict']}, Access: {auth2['access']}")
    print(f"  Missing: {auth2['missing_attributes']}")
    print()
    
    # Test 5: Detect corruption
    print("Test 5: Data Corruption Detection")
    clean_data = {"id": 1, "value": 0.5, "name": "test"}
    corrupted_data = {"id": 1, "value": "wrong_type"}  # missing name, wrong type
    
    schema = {"id": int, "value": float, "name": str}
    
    check1 = anubis.detect_corruption(clean_data, schema)
    print(f"  Clean data: {check1['verdict']}")
    
    check2 = anubis.detect_corruption(corrupted_data, schema)
    print(f"  Corrupted data: {check2['verdict']}")
    print(f"  Corrupted fields: {check2['corrupted_fields']}")
    print()
    
    # Statistics
    print("📊 ANUBIS Statistics:")
    stats = anubis.get_statistics()
    for key, val in stats.items():
        if isinstance(val, float):
            print(f"  {key}: {val:.2f}%")
        else:
            print(f"  {key}: {val}")
    
    print("\n✨ ANUBIS is the gatekeeper.")
    print("   IF (condition) THEN pass ELSE reject")
    print("   Only the validated may proceed.\n")

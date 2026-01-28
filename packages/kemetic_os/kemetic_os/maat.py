"""
MAAT - BALANCE & EQUILIBRIUM SYSTEM
The cosmic law that maintains order

In Kemetic wisdom: Ma'at is truth, justice, balance, cosmic order
Mathematical representation: Ma'at = Σ = 0 (sum of all forces equals zero)

MA'AT enforces balance. When systems drift from equilibrium,
MA'AT corrects them. This is not morality - this is mathematics.
"""

from typing import Dict, Any, List, Tuple, Optional
import math


class MAAT:
    """
    Balance & Equilibrium System
    
    MA'AT maintains cosmic order through:
    - Conservation laws (energy, mass, momentum)
    - Error correction
    - Homeostasis
    - System integrity checks
    - Balance enforcement
    """
    
    def __init__(self, agent_id: str, balance_threshold: float = 0.1):
        self.agent_id = agent_id
        self.balance_threshold = balance_threshold
        
        # The Scales of Ma'at
        self.balance_history = []
        self.corrections_made = 0
        self.violations_detected = 0
        
        # Current balance state
        self.current_balance = 0.0
        self.is_balanced = True
    
    def check_balance(self, system_state: Dict[str, float]) -> Tuple[bool, float]:
        """
        Check if a system is in balance
        
        Ma'at = Σ = 0 (sum equals zero)
        
        For a system to be balanced, the sum of all forces/values
        should equal zero (or be within threshold)
        """
        # Calculate the sum of all values
        total = sum(system_state.values())
        
        # Check if within threshold of zero
        is_balanced = abs(total) <= self.balance_threshold
        
        self.current_balance = total
        self.is_balanced = is_balanced
        
        # Record balance check
        self.balance_history.append({
            "state": system_state.copy(),
            "sum": total,
            "balanced": is_balanced,
            "threshold": self.balance_threshold
        })
        
        if not is_balanced:
            self.violations_detected += 1
        
        return is_balanced, total
    
    def enforce_balance(self, system_state: Dict[str, float]) -> Dict[str, float]:
        """
        Enforce balance on an unbalanced system
        
        When Σ ≠ 0, MA'AT corrects it
        """
        is_balanced, total = self.check_balance(system_state)
        
        if is_balanced:
            # Already balanced, no correction needed
            return system_state
        
        # System is imbalanced - correct it
        corrected_state = self._apply_correction(system_state, total)
        
        self.corrections_made += 1
        
        return corrected_state
    
    def _apply_correction(self, system_state: Dict[str, float], imbalance: float) -> Dict[str, float]:
        """
        Apply correction to restore balance
        
        Distribute the imbalance across all components proportionally
        """
        if len(system_state) == 0:
            return system_state
        
        # Distribute correction proportionally
        correction_per_item = -imbalance / len(system_state)
        
        corrected_state = {
            key: value + correction_per_item
            for key, value in system_state.items()
        }
        
        return corrected_state
    
    def validate_conservation(self, 
                            before_state: Dict[str, float],
                            after_state: Dict[str, float],
                            conserved_property: str = "total") -> bool:
        """
        Validate that a property was conserved across a transformation
        
        Conservation laws: energy, mass, momentum must be preserved
        """
        before_total = sum(before_state.values())
        after_total = sum(after_state.values())
        
        difference = abs(after_total - before_total)
        
        is_conserved = difference <= self.balance_threshold
        
        if not is_conserved:
            self.violations_detected += 1
        
        return is_conserved
    
    def check_homeostasis(self, 
                         current_value: float,
                         target_value: float,
                         tolerance: float = 0.1) -> Tuple[bool, float]:
        """
        Check if a system maintains homeostasis around a target value
        
        Homeostasis = maintaining stable internal conditions
        """
        deviation = abs(current_value - target_value)
        in_homeostasis = deviation <= tolerance
        
        return in_homeostasis, deviation
    
    def restore_homeostasis(self,
                           current_value: float,
                           target_value: float,
                           correction_rate: float = 0.5) -> float:
        """
        Restore homeostasis by moving toward target value
        
        MA'AT gently guides the system back to balance
        """
        deviation = target_value - current_value
        correction = deviation * correction_rate
        
        new_value = current_value + correction
        
        self.corrections_made += 1
        
        return new_value
    
    def weigh_heart(self, heart: float, feather: float = 1.0) -> Dict[str, Any]:
        """
        The Weighing of the Heart ceremony
        
        In Kemetic tradition: heart must be lighter than or equal to feather
        Here: validate that a value meets the balance requirement
        """
        passes = heart <= feather
        difference = heart - feather
        
        judgment = {
            "heart": heart,
            "feather": feather,
            "difference": difference,
            "passes": passes,
            "verdict": "BALANCED" if passes else "IMBALANCED"
        }
        
        if not passes:
            self.violations_detected += 1
        
        return judgment
    
    def calculate_entropy(self, system_state: Dict[str, float]) -> float:
        """
        Calculate system entropy (disorder)
        
        MA'AT seeks to minimize entropy (maintain order)
        """
        if len(system_state) == 0:
            return 0.0
        
        values = list(system_state.values())
        total = sum(values)
        
        if total == 0:
            return 0.0
        
        # Calculate Shannon entropy
        probabilities = [v / total for v in values if v > 0]
        entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
        
        return entropy
    
    def maintain_order(self, system_state: Dict[str, float]) -> Dict[str, Any]:
        """
        Comprehensive order maintenance check
        
        Runs all MA'AT protocols:
        - Balance check
        - Entropy calculation
        - Homeostasis validation
        - Correction if needed
        """
        # Check balance
        is_balanced, total_sum = self.check_balance(system_state)
        
        # Calculate entropy (disorder)
        entropy = self.calculate_entropy(system_state)
        
        # Determine if intervention needed
        needs_correction = not is_balanced or entropy > 3.0
        
        result = {
            "is_balanced": is_balanced,
            "sum": total_sum,
            "entropy": entropy,
            "needs_correction": needs_correction,
            "corrected_state": None
        }
        
        if needs_correction:
            result["corrected_state"] = self.enforce_balance(system_state)
        
        return result
    
    def get_balance_statistics(self) -> Dict[str, Any]:
        """
        Get statistics on balance maintenance
        """
        total_checks = len(self.balance_history)
        balanced_count = sum(1 for b in self.balance_history if b["balanced"])
        
        return {
            "total_balance_checks": total_checks,
            "balanced_count": balanced_count,
            "imbalanced_count": total_checks - balanced_count,
            "corrections_made": self.corrections_made,
            "violations_detected": self.violations_detected,
            "current_balance": self.current_balance,
            "is_currently_balanced": self.is_balanced,
            "balance_rate": balanced_count / total_checks if total_checks > 0 else 0.0
        }
    
    def reset_balance_metrics(self) -> None:
        """
        Reset balance tracking metrics
        """
        self.balance_history = []
        self.corrections_made = 0
        self.violations_detected = 0
        self.current_balance = 0.0
        self.is_balanced = True


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("MA'AT - BALANCE & EQUILIBRIUM SYSTEM")
    print("=" * 60)
    
    # Create MA'AT instance
    maat = MAAT(agent_id="voidchi_001", balance_threshold=0.1)
    
    print("\n⚖️  MA'AT maintains cosmic order...\n")
    
    # Test 1: Balanced system
    print("Test 1: Balanced System")
    balanced_system = {"energy_in": 1.0, "energy_out": -1.0}
    is_balanced, total = maat.check_balance(balanced_system)
    print(f"  System: {balanced_system}")
    print(f"  Sum: {total:.4f}")
    print(f"  Balanced: {is_balanced}")
    print()
    
    # Test 2: Imbalanced system
    print("Test 2: Imbalanced System")
    imbalanced_system = {"energy_in": 2.0, "energy_out": -0.5, "waste": 0.3}
    is_balanced, total = maat.check_balance(imbalanced_system)
    print(f"  System: {imbalanced_system}")
    print(f"  Sum: {total:.4f}")
    print(f"  Balanced: {is_balanced}")
    
    # Enforce balance
    corrected = maat.enforce_balance(imbalanced_system)
    print(f"  Corrected: {corrected}")
    is_balanced_now, total_now = maat.check_balance(corrected)
    print(f"  New Sum: {total_now:.4f}")
    print(f"  Now Balanced: {is_balanced_now}")
    print()
    
    # Test 3: Weighing of the Heart
    print("Test 3: Weighing of the Heart")
    judgment1 = maat.weigh_heart(heart=0.9, feather=1.0)
    print(f"  Heart: {judgment1['heart']}, Feather: {judgment1['feather']}")
    print(f"  Verdict: {judgment1['verdict']}")
    
    judgment2 = maat.weigh_heart(heart=1.5, feather=1.0)
    print(f"  Heart: {judgment2['heart']}, Feather: {judgment2['feather']}")
    print(f"  Verdict: {judgment2['verdict']}")
    print()
    
    # Test 4: Homeostasis
    print("Test 4: Homeostasis Restoration")
    current_temp = 0.3
    target_temp = 0.7
    print(f"  Current: {current_temp}, Target: {target_temp}")
    
    for i in range(5):
        current_temp = maat.restore_homeostasis(current_temp, target_temp, correction_rate=0.3)
        in_homeostasis, deviation = maat.check_homeostasis(current_temp, target_temp)
        print(f"  Step {i+1}: {current_temp:.4f} (deviation: {deviation:.4f}, stable: {in_homeostasis})")
    print()
    
    # Statistics
    print("📊 MA'AT Statistics:")
    stats = maat.get_balance_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n✨ MA'AT enforces balance. Σ = 0. Order is maintained.\n")

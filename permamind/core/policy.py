class DecisionPolicy:
    def choose(self, options):
        scored = [
            (opt["expected_gain"] / max(opt["cost"], 1e-6), opt)
            for opt in options
        ]
        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[0][1] if scored else None

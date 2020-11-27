from ..rule import Preposition, Rule


class InferenceSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def __add__(self, other):
        try:
            antecedents, consecuents = other
        except ValueError:
            raise ValueError("The rule is not in the correct format")
        if not isinstance(antecedents, Preposition):
            raise ValueError("The antecedent is not a Preposition")
        if not isinstance(consecuents, Preposition):
            raise ValueError("The consecuent is not a Preposition")
        self.add_rule(Rule(antecedents, consecuents))
        return self

    def infer(self, **values):
        pass
    
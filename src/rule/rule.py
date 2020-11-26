
from rule.preposition import Preposition

from .preposition import Preposition

class Rule:
    def __init__(self, antecedents, consecuents):
        self.antecedents = antecedents
        self.consecuents = consecuents

    def __call__(self, value):
        return self.consecuents(self.antecedents(value))
from .preposition import Preposition

class BaseRule:
    def __init__(self, antecedents, consecuents):
        self.antecedents = antecedents
        self.consecuents = consecuents

    def __call__(self, values):
        raise NotImplementedError()

class MamdaniLarsenRule(BaseRule):
    def __call__(self, values):
        fuzz_value = self.antecedents(values)
        union = None

        for _, fuzz_set in self.consecuents:
            if union is None:
                union = fuzz_set
            else:
                union |= fuzz_set

        return (fuzz_value, union)
            
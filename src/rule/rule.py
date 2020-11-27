from .preposition import Preposition

class Rule:
    def __init__(self, antecedents, consecuents):
        self.antecedents = antecedents
        self.consecuents = consecuents

    def __call__(self, values):
        fuzz_value = self.antecedents(values)
        union = None
        key = ''
        for k, fuzz_set in self.consecuents:
            key = k
            if union is None:
                union = fuzz_set
            else:
                union |= fuzz_set
        fuzz_value = self.consecuents({key :fuzz_value})

        return (fuzz_value, union)
            
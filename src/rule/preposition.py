
class Preposition:
    def __init__(self, fuz_set):
        self.set = fuz_set

    def __and__(self, other):
        self.set |= other.set
        return self

    def __or__(self, other):
        self.set &= other.set
        return self

    def __invert__(self):
        self.set.membership = lambda x: 1 - self.set.membership(x)

    def __call__(self, value):
        return self.set.membership(value)

class Preposition:
    def __init__(self, fuz_set, name):
        self.sets = {name : fuz_set}
        
    def __and__(self, other):
        return AndPreposition(self, other)

    def __or__(self, other):
        return OrPreposition(self, other)

    def __invert__(self):
        return NotPreposition(self)

    def __call__(self, values):
        for k, v in values.items():
            if k in self.sets:
                return self.sets[k].membership(v)
        raise ValueError('Item not in sets')

    def __iter__(self):
        return iter(self.sets.items())

    def __len__(self):
        return len(self.sets)


class BinaryPreposition(Preposition):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class AndPreposition(BinaryPreposition):
    def __call__(self, values):
        return min(
            self.left(values),
            self.right(values),
        )


class OrPreposition(BinaryPreposition):
    def __call__(self, values):
        return max(
            self.left(values),
            self.right(values),
        )


class NotPreposition(Preposition):
    def __init__(self, prep):
        self.prep = prep

    def __call__(self, values):
        return 1 - self.prep(values)

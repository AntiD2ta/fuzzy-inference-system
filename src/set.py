from .membership import Membership
from numpy import arange

class Set:
    def __init__(self, membership, step):
        self.membership = membership
        self.step = 0.05

    def __or__(a, b):
        #//TODO: Implement union of sets
        pass

    def domain(self):
        d = set(arange(self.membership.items[0], self.membership.items[-1], self.step))
        d.update(set(self.membership.items))
        if len(d) > 100:
            d = list(d)
            d.sort()
        return list(d)

    def __iter__(self):
        return iter(self.domain())

    def __len__(self):
        return len(self.domain())

    def __str__(self):
        pass
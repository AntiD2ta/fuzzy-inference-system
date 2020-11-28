from .mamdani import Mamdani
from ..membership import Membership
from ..set import Set

def make_membership(fuzz_value, fuzz_set):
    return  Membership(
                lambda x: fuzz_set.membership(x) * fuzz_value,
                fuzz_set.membership.items
            )

class Larsen(Mamdani):
    def fuzzyfication(self, values):
        sets = []
        for r in self.rules:
            fuzz_value, fuzz_set = r(values)

            memb = make_membership(fuzz_value, fuzz_set)
            new_set = Set(memb, fuzz_set.step, name=f'{fuzz_set.name} times {fuzz_value}', var=fuzz_set.var)
            sets.append(new_set)
        
        return sets

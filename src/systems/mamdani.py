from .system import InferenceSystem
from ..membership import Membership
from ..defuzzification import centroid_defuzzification
from ..set import Set


class Mamdani(InferenceSystem):
    def aggregate(self, fuzz_sets):
        union = None
        for s in fuzz_sets:
            if union is None:
                union = s
            else:
                union |= s

        return union

    def fuzzyfication(self, values):
        sets = []
        for r in self.rules:
            fuzz_value, fuzz_set = r(values)

            memb = Membership(
                lambda x: min (fuzz_set.membership(x), fuzz_value),
                fuzz_set.membership.items
            )
            new_set = Set(memb, fuzz_set.step, name=f'{fuzz_set.name} truncated by {fuzz_value}')
            sets.append(new_set)
        
        return sets

    def infer(self, defuzz=centroid_defuzzification, graph=False, **values):
        fuzz_sets = self.fuzzyfication(values)
        if graph:
            for s in fuzz_sets:
                s.graph()
        aggr_set = self.aggregate(fuzz_sets)
        if graph:
            aggr_set.graph()
        return defuzz(aggr_set)


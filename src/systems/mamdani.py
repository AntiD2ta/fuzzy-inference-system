from .system import InferenceSystem
from ..membership import Membership
from ..defuzzification import centroid_defuzzification
from ..set import Set
from ..rule import BaseRule, MamdaniLarsenRule


def make_membership(fuzz_value, fuzz_set):
    return  Membership(
                lambda x: min (fuzz_set.membership(x), fuzz_value),
                fuzz_set.membership.items
            )

class Mamdani(InferenceSystem):
    def add_rule(self, rule: BaseRule):
        self.rules.append(MamdaniLarsenRule(rule.antecedents, rule.consecuents))

    def aggregate(self, fuzz_sets):
        unions = dict()
        for s in fuzz_sets:
            if s.var not in unions:
                unions[s.var] = s
            else:
                unions[s.var] |= s

        for k, s in unions.items():
            s.name = f'Aggregation of {k}'
        return unions

    def fuzzyfication(self, values):
        sets = []
        for r in self.rules:
            fuzz_value, fuzz_set = r(values)

            memb = make_membership(fuzz_value, fuzz_set)

            new_set = Set(memb, fuzz_set.step, name=f'{fuzz_set.name} truncated by {fuzz_value}', var=fuzz_set.var)
            sets.append(new_set)
           
        return sets

    def infer(self, defuzz=centroid_defuzzification, graph=False, **values):
        fuzz_sets = self.fuzzyfication(values)
        if graph:
            for s in fuzz_sets:
                s.graph()
        aggr_sets = self.aggregate(fuzz_sets)
        if graph:
            for s in aggr_sets.values():
                s.graph()
        results = []
        for k, s in aggr_sets.items():
            results.append((k, defuzz(s)))
        return results


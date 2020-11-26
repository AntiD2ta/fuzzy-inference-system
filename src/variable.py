from .membership import Membership
from .set import Set
from .rule import Preposition
from numpy import NaN

class Var():
    '''
    Linguistic variable
    '''
    def __init__(self, name):
        self.name = name
        self.sets = dict()

    def __add__(self, arg):
        if len(arg) == 2:
            term, memb = arg
            step = NaN
        else:
            term, memb, step = arg

        self.add_term(term, memb, step)
        return self

    def add_term(self, term, memb, step=NaN):
        if step == NaN:
            new_set = Set(memb, name=term)
        else:
            new_set = Set(memb, step, name=term)
        self.sets[term] = new_set

    def Is(self, name):
        fuz_set = self.sets[name]
        set_copy = Set(fuz_set.membership, fuz_set.step, fuz_set.name)
        return Preposition(set_copy)

    def __str__(self):
        return self.name + '\n' + str(self.sets) 

from .membership import Membership
from .set import Set
from .rule import Preposition
from numpy import NaN

import matplotlib.pyplot as plt

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
            step = None
        else:
            term, memb, step = arg

        self.add_term(term, memb, step)
        return self

    def add_term(self, term, memb, step=None):
        if step is None:
            new_set = Set(memb, name=term, var=self.name)
        else:
            new_set = Set(memb, step, name=term, var=self.name)
        self.sets[term] = new_set

    def Is(self, name):
        try:
            fuz_set = self.sets[name]
        except KeyError:
            raise Exception(f'{name} is not a valid term of {self.name} Variable')
        set_copy = Set(fuz_set.membership, fuz_set.step, fuz_set.name, fuz_set.var)
        return Preposition(set_copy, self.name)

    def __str__(self):
        return self.name + '\n' + str(self.sets) 

    def graph(self):
        plots = []
        plt.figure()
        for it, desc in enumerate(self.sets.values()):
            x_data = desc.domain()
            y_data = [desc.membership(x) for x in x_data]
            plots.append(plt.plot(x_data, y_data, f"C{it+1}", label=desc.name))
        plt.legend()
        plt.title(self.name)
        plt.savefig(f"var_{self.name}.png")
        
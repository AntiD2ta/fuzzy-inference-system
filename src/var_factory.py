from .variable import Var

class VarFactory():
    def _make_variable(self, name):
        try:
            self.vars
        except AttributeError:
            self.vars = dict()

        if name in self.vars:
            raise Exception(f'There is a Variable with name {name} already')

        self.vars[name] = Var(name)
        return self.vars[name]

factory = VarFactory()

def make_variable(name):
    return factory._make_variable(name)
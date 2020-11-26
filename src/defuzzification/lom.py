from .utils import get_maximums

def lom_defuzzification(set):
    return get_maximums(set)[-1]

from .utils import get_maximums

def som_defuzzification(set):
    return get_maximums(set)[0]

from .utils import get_maximums

def mom_defuzzification(set):
    maximums = get_maximums(set)
    return (maximums[0] + maximums[-1]) / 2
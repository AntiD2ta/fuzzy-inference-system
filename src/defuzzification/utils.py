
def get_maximums(set):
    fuz_set = [(set.membership(x), x) for x in set]
    fuz_set.sort()
    fuz_set = [x for (ux, x) in fuz_set if ux == fuz_set[-1][0]]
    fuz_set.sort()
    return fuz_set
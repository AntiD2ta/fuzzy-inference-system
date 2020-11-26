
def centroid_defuzzification(set):
    numerator = 0
    denominator = 0
    for value in set:
        numerator += value * set.membership(value)
        denominator += set.membership(value)
    return numerator / denominator
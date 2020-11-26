from .membership import Membership
from .s import SMembership
from .z import ZMembership


class GaussianMembership(Membership):
    def __init__(self, b, d):
        def func(x):
            s = SMembership(b - d, b)
            z = ZMembership(b, b + d)
            if x <= b:
                return s(x)
            return z(x)

        super(GaussianMembership, self).__init__(func, [b - d, b, b + d])

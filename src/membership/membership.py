
class Membership:
    def __init__(self, function, items: list):
        self.function = function
        self.items = items

    def __call__(self, value):
        return self.function(value)
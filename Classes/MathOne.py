import math


class MathOne:

    sum = None  # type: int
    x = None  # type : int
    y = None    # type : int

    def __init__(self):
        pass

    def add(self, x, y):
        self.x = x
        self.y = y
        self.sum = self.x + self.y
        return self.sum


if __name__ == '__main__':
    m1 = MathOne()
    print(m1.add(4, 5))
import math
from functools import partial, lru_cache


def power(x, y):
    return math.pow(x, y)


p = partial(power, y=2)
print(p(2))
print(p(4))
print(p(8))

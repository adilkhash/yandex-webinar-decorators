from functools import wraps
import time

"""
LEGB
"""


def dollar_decorator(func=None, divide_by=1_000_000):

    def wrapper(f):
        @wraps(f)
        def _decorator(*args, **kwargs):
            result = f(*args, **kwargs)
            return result / divide_by
        return _decorator

    if func and callable(func):
        return wrapper(func)

    return wrapper


@dollar_decorator(divide_by=1)
def get_reveue(dollars):
    return int(dollars * 1_000_000)


print(get_reveue(55.33))

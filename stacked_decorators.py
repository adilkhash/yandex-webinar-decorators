import time
from functools import wraps


def log_exception(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f()
        except Exception as e:
            print(f'Exception: {e}')
    return wrapper


def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f()
        end = time.time() - start
        print(f'Function {f.__name__} was executed in {end} seconds')
        return result
    return wrapper


@timer
@log_exception
def do_work():
    return 1

do_work()

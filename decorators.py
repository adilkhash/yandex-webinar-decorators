from typing import Callable
from django.contrib.auth.decorators import login_required


def decorator(func: Callable):
    def wrapper(msg):
        print(f'Calling {func.__name__}')
        func(msg)
        print('End of decorator')
    return wrapper


@decorator
def say_something(msg: str):
    print(msg)


def parametrized_decorator(func: Callable = None, param: str = None):
    def _decorator(func: Callable):
        def wrapper(*args, **kwargs):
            print(f'Calling {func.__name__}')
            print(f'Decorator {param=}')
            func(*args, **kwargs)
        return wrapper
    if func and callable(func):
        return _decorator(func)
    return _decorator


@parametrized_decorator(param='my_param')
def func():
    print('This is func')


@parametrized_decorator
def func2():
    print('This is func')


if __name__ == '__main__':
    func()
    func2()
    say_something('hello')

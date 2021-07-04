

class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Arguments:', *args, **kwargs)
        print('Hello from class-decorator')
        self.func(*args, **kwargs)


@Decorator
def func(msg):
    print(msg)


f = Decorator(func)


class A:
    def __init__(self, a):
        self.a = a

    def __call__(self, *args, **kwargs):
        return 1




def repr_decorator(cls):
    def wrapper():

        def _repr(self):
            return f'[{self.__class__.__name__}]'
        cls.__repr__ = _repr
        return cls

    return wrapper()


@repr_decorator
class CashCalculator:
    USD_RATE: int = 70
    EUR_RATE: int = 80

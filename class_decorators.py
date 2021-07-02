class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Calling {self.func.__name__}')
        return self.func(*args, **kwargs)


@Decorator
def say(msg):
    print(msg)
    return 1


def class_decorator(cls):
    def wrapper():
        def __repr__(self):
            keys = self.__annotations__.keys()
            params = ', '.join([f'{key}={getattr(self, key, None)}' for key in keys])
            return f'<Name: {self.__class__.__name__} {params}>'
        cls.__repr__ = __repr__
        cls.__str__ = __repr__
        return cls
    return wrapper()


@class_decorator
class A:
    x: int = 1
    y: int = 2


@class_decorator
class CurrencyCalculator:
    USD_RATE: float = 70
    EUR_RATE: float = 80


x = CurrencyCalculator()
print(x)


def method_decorator(name, func):
    def wrapper(cls):
        def _dec(*args, **kwargs):
            instance = cls(*args, **kwargs)
            if hasattr(instance, name):
                method = getattr(instance, name)
                setattr(instance, name, func(method))
            return instance
        return _dec
    return wrapper


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'calling method: {func.__name__}')
        return func(*args, **kwargs)
    return wrapper


@method_decorator(name='hello', func=decorator)
class MyClass:
    def say(self, msg):
        print(msg)

    def hello(self):
        return f'{self.__class__.__qualname__}'


x = MyClass()
print(x.hello())

classes = []


def register(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, *kwargs)
        classes.append(instance)
    return wrapper


@register
class A:
    pass


@register
class B:
    pass


A()
B()

print(classes)

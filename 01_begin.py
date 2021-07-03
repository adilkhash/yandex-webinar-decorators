from django.utils.decorators import method_decorator

def simple_decorator(f):
    return f


@simple_decorator
def function():
    print('hello')

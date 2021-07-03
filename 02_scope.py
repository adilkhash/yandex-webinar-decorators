"""
Область видимости указывает на контекст переменной в котором её можно использовать
Существует локальный контекст и глобальный

Правило LEGB:

L - Local
E - Enclosing
G - Global
B - Built-ins

"""

outer_var = 2


def func():
    outer_var = 1

    def inner_func():
        print(f'inner_func = {outer_var=}')

    inner_func()
    print(f'func = {outer_var=}')


func()

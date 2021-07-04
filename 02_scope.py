"""
Область видимости указывает на контекст переменной в котором её можно использовать
Существует локальный контекст и глобальный

Правило LEGB:

L - Local
E - Enclosing
G - Global
B - Built-ins
"""

var = 1

def func():
    var = 2

    def inner_func():
        nonlocal var
        print(var)

    inner_func()

func()

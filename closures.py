"""
Замыкание это функция, ссылающаяся на переменные внешней функции (вне локального контекста)
LEGB

Local
Enclosing
Global
Built-in
"""


def func():
    calls = 0

    def _inner():
        nonlocal calls
        calls = calls + 1
        return calls

    return _inner


f = func()
f()
f()
f()
n = f()
print(n)

y = func()
x = y()
print(x)

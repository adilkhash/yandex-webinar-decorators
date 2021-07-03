"""
Замыкание это функция, ссылающаяся на переменные внешней функции (вне локального контекста)
"""

def counter():
    count = 0

    def _counter():
        nonlocal count
        count += 1
        return count
    return _counter


if __name__ == '__main__':
    f = counter()
    f2 = counter()

    f()
    f()
    f()
    f()
    n = f()
    print(n)
    print(f2())

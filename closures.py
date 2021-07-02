
def counter():
    count = 0

    def _counter():
        nonlocal count
        count += 1
        return count
    return _counter


if __name__ == '__main__':
    f = counter()
    f()
    f()
    f()
    f()
    n = f()
    print(n)

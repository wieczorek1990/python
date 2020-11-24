def fibonacci(n):
    if n < 0:
        raise ValueError()
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    x, y = 0, 1
    current = 0
    for i in range(2, n + 1):
        current = x + y
        x, y = y, current
    return current


for i in range(8):
    print(fibonacci(i))


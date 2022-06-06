def powerful(a, b):
    first = a ** b
    return first >= 2 * b ** 2 and first >= (a * b) ** 2


input_ = raw_input('Enter: ')
a, b = input_.split(' ')
a, b = map(int, (a, b))
print(powerful(a, b))


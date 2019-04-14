print(filter(lambda x: x == 0, (0, 1, 2, 0)))

a = [{'a': 0, 'b': 1}, {'a': 1, 'b': 2}]
from operator import itemgetter
print(list(reversed(sorted(a, key=itemgetter('b')))))
print(list(reversed(sorted(a, key=lambda a: a['b']))))

a = [1, 2, 3, 4]
print(map(lambda x: x ** 2, a))

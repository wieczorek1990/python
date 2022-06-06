from functools import wraps
from time import perf_counter


def perf_counter_decorator(f):
    def wrapper(*args, **kwargs):
        start_counter = perf_counter()
        result = f(*args, **kwargs)
        end_counter = perf_counter()
        print(f'Elapsed {end_counter - start_counter}')
        return result
    return wrapper


@perf_counter_decorator
def hello():
    print('Hello!')


hello()


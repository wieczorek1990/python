from functools import wraps


def decorator(name):
    print('inside decorator: %s' % name)
    def outer_wrapper(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print('inside wrapper: before')
            result = f(*args, **kwargs)
            print('inside wrapper: after')
            return result
        return wrapper
    return outer_wrapper


@decorator('A')
def function_a():
    print('inside function A')
    return 1


@decorator('B')
def function_b():
    print('inside function B')
    return 2


result = function_a()
print('after function: %i' % result)

result = function_b()
print('after function %i' % result)


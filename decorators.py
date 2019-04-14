from functools import wraps

def decorator(name):
    print('inside decorator: %s' % name)
    def outer_wrapper(f):
        def wrapper(*args, **kwargs):
            print('inside wrapper: before')
            result = f(*args, **kwargs)
            print('inside wrapper: after')
            return result
        return wrapper
    return outer_wrapper

@decorator('hello world')
def function():
    print('inside function')
    return 1

result = function()
print('after function: %i' % result)

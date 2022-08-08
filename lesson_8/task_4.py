def val_checker(callback):
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not callback(arg): raise ValueError(f'wrong val {arg}')
            return func(*args, **kwargs)
        return wrapper
    return _wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3




def type_logger(func):
    def log_wrapper(*args, **kwargs):
        print(f'Call for: {func.__name__}')
        
        for i, arg in enumerate(args):
            print(f'{arg}: {type(arg)}', end='')
            if i + 1 < len(args): print(', ', end='')
        if len(args): print('')
        for i, (key, value) in enumerate(kwargs.items()):
            print(f"'{key}' = {value}: {type(value)}", end='')
            if i + 1 < len(kwargs): print(', ', end='')
        if len(kwargs): print('')

        res = func(*args, **kwargs)
        
        print(f'Rezult: {res}\ttype: {type(res)}')        
        return res
    return log_wrapper


@type_logger
def render_input(*args, **kwargs):
    return 1

@type_logger
def calc_cube(x):
    return x ** 3

render_input()

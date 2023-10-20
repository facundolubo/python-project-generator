def decorator_function(function_to_decorate):
    def wrapper_function(*args, **kwargs):
        print(f'Running {function_to_decorate.__name__}')
        return function_to_decorate(*args, **kwargs)
    function_to_decorate.__name__ = 'tuvieja'
    return wrapper_function

@decorator_function
def display_name(name):
    display_name.__name__ = name
    print(f'Hello from {display_name.__name__}')

display_name('')
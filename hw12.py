import re
#1
def logger(func):
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(repr, args))
        kwargs_str = ', '.join(f'{key}={value!r}' for key, value in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        print(f'{func.__name__} called from {all_args}')
        return func(*args, **kwargs)
    
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


result_add = add(4, 5)
result_square_all = square_all(2, 3, 4)

#2
def stop_words(words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = re.sub(rf'\b{re.escape(word)}\b', '*', result, flags=re.IGNORECASE)
            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} we are drinking pepsi in our new BMW!"


assert create_slogan("Steve") == "Steve we are drinking * in our new *!"


#1
def count_local_variables(func):
     local_variables = func.__code__.co_varnames[:func.__code__.co_argcount]
     print(f"Number of local variables in function {func.__name__}: {len(local_variables)}")
     print("Names of local variables:", local_variables)
def example_function():
    a = 1
    b = 2
    c = a + b
    print(c)
count_local_variables(example_function)

#2
def outer_function(message):
    
    def inner_function():
        print(message)

    return inner_function

my_closure = outer_function("Hello, it's a short circuit!")

my_closure()
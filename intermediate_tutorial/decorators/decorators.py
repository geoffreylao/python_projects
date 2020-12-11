# @mydecorator # decorator syntax, decorator is a function takes another function as an arguement and extends its function
# def dosomething():
#     pass

import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs): # can use as many arguments and keyword arguements as you want
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

print_name()

@start_end_decorator
def add5(x):
    return x + 5

print(add5(10))
print(help(add5)) # confirm identity of function
print(add5.__name__)


# decorators with arguements
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('Akex')

# decorators nested

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello('Alex')

# class decorators

class CountCalls:
    def __init__(self, func):
        self.func = func # member variable
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'this is excecuted {self.num_calls} times')
        return self.func(*args, **kwargs)

# cc = CountCalls(None)
# cc()

@CountCalls
def say_hi():
    print('hi')

say_hi()
say_hi()
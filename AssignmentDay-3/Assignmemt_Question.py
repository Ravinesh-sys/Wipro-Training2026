import time
import functools

def execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__} executed in {end_time - start_time:.8f}s")
        return result
    return wrapper

@execution_time
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

number = 2
result = factorial(number)
print(f"Factorial of {number} is {result}")
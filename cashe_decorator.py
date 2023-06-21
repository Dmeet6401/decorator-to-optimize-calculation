from functools import wraps
from time import perf_counter
import sys


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]
    return wrapper



@memoize
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@memoize
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    start = perf_counter()
    f = fibonacci(80)
    end = perf_counter() 
    print(f)
    print(f"{end - start}")
    # took 0.00028150000000000397 to calculate

    start = perf_counter()
    fa = factorial(50)
    end = perf_counter() 
    print(fa)
    print(f"{end - start}")

    # O/p = 30414093201713378043612608166064768844377641568960512000000000000
    #Time = 0.00017790000000000167

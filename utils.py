"""Utility functions"""


from time import time


def print_timed(func):
    start = time()
    print(f"{func.__name__}() = {func()}")
    end = time()
    print(f"Time elapsed = {end - start:.6f}s")


def is_prime(num):
    if num>1:
        for i in range(2, int(num/2)+1):
            if (num % i == 0):
                return False
            
        else:
            return True
        
    else:
        return False
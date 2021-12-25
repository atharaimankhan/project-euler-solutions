"""Utility functions"""


from time import time


def print_timed(func):
    start = time()
    print(f"{func.__name__}() = {func()}")
    end = time()
    print(f"Time elapsed = {end - start:.6f}s")


def is_prime(num):
    if num==2 or num==3: return True
    if num%2==0 or num<2: return False
    for i in range(3, int(num**0.5)+1, 2):
        if (num % i == 0):
            return False
        
    else:
        return True

def count_factors(num:int):
    if num<=0:
        return None
    if num==1:
        return 1
    count = 2               # 1 and number itself counts 2 
    for i in range(2,int(num**0.5)+1):         # we start from 2 and check till the half of the number
        if(num%i==0):
            if num/i == i:
                count+=1
            else:
                count+=2
    return count
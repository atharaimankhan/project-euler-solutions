"""
Problem 23

URL: https ://projecteuler.net/problem=23

"""


from utils import is_abundant, print_timed, sum_of_proper_divisors
from itertools import product


def problem23():
    sum=0

    abundant_numbers = []

    for i in range(1, 28123):
        if is_abundant(i):
            abundant_numbers.append(i)
    
    res =0
    sums = set()
    
    for num1 in abundant_numbers:
        for num2 in abundant_numbers:
            sums.add(num1+num2)
            


    for num in range(1, 28123):
        
        if num not in sums:
            res+=num
        
        
    return res

if __name__ == '__main__':
    
    print_timed(problem23)



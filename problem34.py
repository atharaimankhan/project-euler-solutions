"""
Problem 34
URL: https://projecteuler.net/problem=34

"""


from utils import count_factors, print_timed
from math import factorial

def problem34():
    total_sum = 0
    for i in range(3,999999):
        sum = 0
        for d in str(i):
            sum += factorial(int(d))
        if sum == i:
            total_sum += i
    return total_sum

if __name__ == '__main__':
    
    print_timed(problem34)

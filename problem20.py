"""
Problem 20

URL: https://projecteuler.net/problem=20

"""


from utils import print_timed
from math import factorial

def problem20():

    fact = factorial(100)
    str_fact = str(fact)

    sum =0
    for digit in str_fact:
        sum += int(digit)
    
    return sum

if __name__ == '__main__':
    
    print_timed(problem20)

"""
Problem 30

URL: https://projecteuler.net/problem=30

"""


from utils import print_timed
from itertools import product

def problem30():

    digits = ['0','1','2','3','4','5','6','7','8','9']

    combs = list(product(digits, repeat=6))

    res = []
    for x in combs:
        num = int(''.join(x))

        s = 0
        for digit in x:
            s += int(digit)**5

        if s == num:
            res.append(num)

    return sum(res)-1           # 1 not included thats why we need to minus 1
if __name__ == '__main__':
    
    print_timed(problem30)

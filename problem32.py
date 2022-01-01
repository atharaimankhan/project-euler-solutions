"""
Problem 32

URL: https://projecteuler.net/problem=32

"""


from utils import is_pandigital, print_timed
from itertools import permutations


def problem32():


    products = set()

    for i in range(1,9999):
        for j in range(1,i):
            n_digits = len(str(i))+len(str(j))+len(str(i*j))
            if n_digits==9:
                if is_pandigital(int(str(i)+str(j)+str(i*j))):
                    products.add((i*j))
            elif n_digits>9:
                break

    return sum(products)

if __name__ == '__main__':
    
    print_timed(problem32)

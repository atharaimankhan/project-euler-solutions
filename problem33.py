"""
Problem 33

URL: https://projecteuler.net/problem=33

"""


from utils import print_timed, remove_identical_digit_in
from fractions import Fraction

def problem33():

    res = []
    n_product = 1
    d_product = 1
    for d in range(11, 100):
        for n in range(11, d):
            i = remove_identical_digit_in(n,d)
            if i != -1:
                if (n/d == i[0]/i[1] and n!=i[0]):
                    n_product *= n
                    d_product *= d
    
    f = Fraction(f'{n_product}/{d_product}')
    return f.denominator


if __name__ == '__main__':
    
    print_timed(problem33)

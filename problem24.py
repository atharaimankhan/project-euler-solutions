"""
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

URL: https://projecteuler.net/problem=24

"""


from utils import print_timed
from itertools import permutations

def problem24():

    digits = [0,1,2,3,4,5,6,7,8,9]

    return int(''.join(list(map(str,list(permutations(digits,10))[1000000-1]))))

if __name__ == '__main__':
    
    print_timed(problem24)

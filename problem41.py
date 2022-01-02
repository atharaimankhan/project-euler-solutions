"""
Problem 41

URL: https://projecteuler.net/problem=41

"""


from utils import is_pandigital_new, is_prime, print_timed


def problem41():

    res = []
    for i in range(1234567, 7654321,2):
        if is_pandigital_new(i):
            if is_prime(i):
                res.append(i)
    
    return res[-1]
    
if __name__ == '__main__':
    
    print_timed(problem41)

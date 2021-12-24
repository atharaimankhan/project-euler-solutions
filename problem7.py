"""
Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

URL: https://projecteuler.net/problem=7
"""


from utils import is_prime, print_timed

def problem7():
    count = 0
    num = 2
    while count!=10001:
        if is_prime(num):
            count +=1
        num +=1
    return num-1

if __name__ == '__main__':
    print_timed(problem7)

"""
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

URL: https://projecteuler.net/problem=21

"""


from utils import print_timed, sum_of_proper_divisors


def problem21():

    amicable_numbers = []

    for a in range(220, 10000):
        if a not in amicable_numbers:
            b = sum_of_proper_divisors(a)
            if(a!=b and sum_of_proper_divisors(b)==a):
                amicable_numbers.append(a)
                amicable_numbers.append(b)
    
    return sum(amicable_numbers)


if __name__ == '__main__':
    
    print_timed(problem21)

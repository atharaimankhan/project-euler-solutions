"""
Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

"""


from utils import is_prime, print_timed

def problem10():
    sum = 17

    for i in range(11, 2000000, 2):
        if is_prime(i):
            sum += i
        
    return sum


    
    


if __name__ == '__main__':
    print_timed(problem10)

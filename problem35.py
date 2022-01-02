"""
Problem 35

URL: https://projecteuler.net/problem=35

"""


from utils import is_prime, print_timed


def problem35():
    circular_primes_count = 0
    for i in range(2,1000000):
        str_i = str(i)
        l = len(str_i)
        if is_prime(i):
            for j in range(1,l):
                if not is_prime(int(str_i[j:l]+str_i[0:j])):
                    break
            else:
                circular_primes_count+=1

    return circular_primes_count
if __name__ == '__main__':
    
    print_timed(problem35)

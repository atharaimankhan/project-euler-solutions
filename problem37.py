"""
Problem 37

URL: https://projecteuler.net/problem=37

"""


from utils import is_prime, print_timed


def problem37():

    truncable_primes = []
    i = 11
    while len(truncable_primes)<11:
        str_i = str(i)
        if is_prime(i):
            for j in range(1,len(str_i)):
                if not is_prime(int(str_i[j:])) or not is_prime(int(str_i[:j])):
                    break
            else:
                truncable_primes.append(i)
        i+=1

    return sum(truncable_primes)
if __name__ == '__main__':
    
    print_timed(problem37)

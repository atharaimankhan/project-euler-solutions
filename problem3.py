"""
Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""


from utils import print_timed
from utils import is_prime


def problem3(n=600851475143):

    if(is_prime(n) or n==1) :   # if input is a prime number itself then we should return it back
        return n
    
    prime_factors = set()       # to get all the factors we can use list.. but we only need to find the max so we dont have to store all duplicate factors. So we use set for this specific problem
    i = 2
    while i <= n:
        if ( n%i==0 and is_prime(i)):      #using is_prime function from utils ..      
            prime_factors.add(i)
            n= n/i
            if(n==1):
                break
            i = 2
        else:
            i+=1
        
        
                
    return max(prime_factors)

if __name__ == '__main__':
    print_timed(problem3)

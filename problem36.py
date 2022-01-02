"""
Problem 36

URL: https://projecteuler.net/problem=36

"""


from utils import is_palindrome, print_timed


def problem36():
    double_base_palindromes = []
    for i in range(1000000):
        binary = int(bin(i)[2:])
        if is_palindrome(i) and is_palindrome(binary):
            double_base_palindromes.append(i)
        
    return sum(double_base_palindromes)
    
    pass
    
if __name__ == '__main__':
    
    print_timed(problem36)

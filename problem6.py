"""
Problem 6:
URL: https://projecteuler.net/problem=6
"""


from utils import print_timed

def problem6():
    
    n = 100
    square_of_sum = 0
    sum_of_squares = (n*(n+1)*(2*n+1))/6
    for i in range(1,n+1):   
        square_of_sum += i
    
    square_of_sum *= square_of_sum

    diff = square_of_sum - sum_of_squares
    return diff

if __name__ == '__main__':
    print_timed(problem6)

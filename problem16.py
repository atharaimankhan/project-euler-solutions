"""
Problem 16:
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?

URL: https://projecteuler.net/problem=16

"""


from utils import print_timed

def problem16():
    
    num = 2**1000
    sum=0
    for i in str(num):
        sum+=int(i)
    
    return sum

if __name__ == '__main__':
    
    print_timed(problem16)

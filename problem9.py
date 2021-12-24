"""
Problem 9:

URL: https://projecteuler.net/problem=9
"""


from utils import print_timed

def problem9():
    
    for c in range(5,1001):
        for b in range(4,c):
            for a in range(3,b):
                if (c*c == b*b + a*a and a+b+c ==1000):
                    return c*b*a
    


if __name__ == '__main__':
    print_timed(problem9)

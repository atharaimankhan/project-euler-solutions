"""
Problem 39

URL: https://projecteuler.net/problem=39

"""


from utils import print_timed
from math import sqrt

def problem39():

    res = {}
    for a in range(1,999):
        for b in range(1,a):
            p = a+b + sqrt(a**2+b**2)
            if (p.is_integer() and p<=1000):
                if p in res:
                    res[p] +=1
                else:
                    res[p] = 1
    
    return int(max(res, key=res.get))

    return res
if __name__ == '__main__':
    
    print_timed(problem39)

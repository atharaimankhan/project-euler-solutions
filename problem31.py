"""
Problem 31

URL: https://projecteuler.net/problem=31

"""

from utils import print_timed
from itertools import combinations_with_replacement

def problem31():

    # 200a+100b+50c+20d+10e+5f+2g+h=200
    res = 0

    for a in range(200,-1,-200):
        for b in range(a,-1,-100):
            for c in range(b,-1,-50):
                for d in range(c,-1,-20):
                    for e in range(d,-1,-10):
                        for f in range(e,-1,-5):
                            for g in range(f,-1,-2):
                                    res+=1

    return res

    # coins = [0,1,2,5,10]

    # res = set()

    # combination_list = combinations_with_replacement(coins, 10)
    
    # for x in combination_list:
    #     if sum(x) == 10:
    #         res.add(x)

    # return len(res)


    


if __name__ == '__main__':
    
    print_timed(problem31)

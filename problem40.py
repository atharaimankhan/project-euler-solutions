"""
Problem 40

URL: https://projecteuler.net/problem=40

"""


from utils import print_timed
from math import prod

def problem40():

    # a = ''

    # # for loop
    # for i in range(1, 185186):
    #     a += str(i)

    # # d1
    # d1 = int(a[0])

    # # d10
    # d10 = int(a[9])

    # # d100
    # d100 = int(a[99])

    # # d1000
    # d1000 = int(a[999])

    # # d10000
    # d10000 = int(a[9999])

    # # d100000
    # d100000 = int(a[99999])

    # # d1000000
    # d1000000 = int(a[999999])

    # # printing the solution
    # print (d1,d10,d100,d1000,d10000,d100000,d1000000)
    
    i = 1
    d = 0
    res = []
    while True:
        str_i = str(i)
        for s in str_i:
            d+=1
            if d in (1,10,100,1000,10000,100000,1000000):
                res.append(int(s))   
                if len(res) == 7:
                    return prod(res)       
        i+=1
    
    
if __name__ == '__main__':
    
    print_timed(problem40)

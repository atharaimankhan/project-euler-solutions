"""
Problem 27

URL: https://projecteuler.net/problem=19

"""


from utils import is_prime, print_timed


def problem27():

    l = []
    for a in range(-999,1000):
        for b in range(-1000,1001):
            n = 0
            while True:
                if(not is_prime(n**2 + a*n + b)):
                    l.append((a,b,n))
                    break
                else:
                    n+=1
            

    res =  max(l, key=lambda x:x[2])
    return res[0]*res[1]
    pass
    
if __name__ == '__main__':

    print_timed(problem27)
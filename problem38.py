"""
Problem 38

URL: https://projecteuler.net/problem=38

"""


from utils import print_timed, is_pandigital


def problem38():

    res = []
    for n in range(100000000,999999999):
        if n == 932718654:
            i = 2
            s = str(n)
            while is_pandigital(s) :
                if len(s)==9:
                    res.append(n)
                if is_pandigital(n*i) and is_pandigital(int(s+str(n*i))):
                    s += str(n*i)
                    i+=1
                else:
                    break
            
        
    return max(res)
    pass
if __name__ == '__main__':
    
    print_timed(problem38)

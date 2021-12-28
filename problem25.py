"""
Problem 25

URL: https://projecteuler.net/problem=25

"""


from utils import print_timed


def problem25():

    a = 0
    b = 1
    index = 0
    while True:
        if len(str(a)) == 1000:
            break
        temp = a + b
        a = b
        b = temp
        index += 1
    
    return index
    

if __name__ == '__main__':
    
    print_timed(problem25)

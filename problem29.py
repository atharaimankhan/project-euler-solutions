"""
Problem 29

URL: https://projecteuler.net/problem=29

"""


from utils import print_timed


def problem29():
    seq = []
    for a in range(2,101):
        for b in range(2,101):
            seq.append(a**b)
    
    return len(set(seq))
    pass
if __name__ == '__main__':
    
    print_timed(problem29)

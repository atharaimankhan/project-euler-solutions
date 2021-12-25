"""
Problem 13:

URL: https://projecteuler.net/problem=13

"""


from utils import print_timed


def problem13():
    
    with open('problem13.txt','r') as f:
        numbers_text = f.readlines()
        numbers = list(map(int, numbers_text))
        return str(sum(numbers))[:10]


if __name__ == '__main__':
    
    print_timed(problem13)

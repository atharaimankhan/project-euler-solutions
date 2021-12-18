"""Problem 1"""

from utils import print_timed


def problem1():
    return sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)

if __name__ == '__main__':
    print_timed(problem1)  # Note: the argument is a *function*, not the result of the function!

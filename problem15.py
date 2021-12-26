"""
Problem 15:
URL: https://projecteuler.net/problem=15

"""


import itertools
from utils import print_timed
from math import factorial

def problem15():
    

    grid_row= 20
    grid_col= 20
    total_steps = grid_row+grid_col        
    # steps = []
    # for i in range(grid_row):
    #     steps.append('R')
    # for i in range(grid_col):
    #     steps.append('D')
    # comb = itertools.permutations(steps,total_steps)
    # return len(list(set(comb)))

    

    number_of_routes = factorial(total_steps)/(factorial(grid_row)*factorial(total_steps-grid_row))
    
    return number_of_routes

if __name__ == '__main__':
    
    print_timed(problem15)

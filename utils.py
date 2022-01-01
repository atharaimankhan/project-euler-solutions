"""Utility functions"""


from time import time


def print_timed(func):
    start = time()
    print(f"{func.__name__}() = {func()}")
    end = time()
    print(f"Time elapsed = {end - start:.6f}s")


def is_prime(num):
    if num==2 or num==3: return True
    if num%2==0 or num<2: return False
    for i in range(3, int(num**0.5)+1, 2):
        if (num % i == 0):
            return False
        
    else:
        return True

def count_factors(num:int):
    if num<=0:
        return None
    if num==1:
        return 1
    count = 2               # 1 and number itself counts 2 
    for i in range(2,int(num**0.5)+1):         
        if(num%i==0):
            if num/i == i:
                count+=1
            else:
                count+=2
    return count

def sum_of_proper_divisors(num:int):
    if num<=0:
        return None
    if num==1:
        return 1
    sum=1      
    for i in range(2,int(num**0.5)+1):         
        if(num%i==0):
            sum += i 
            if i != int(num/i):
                sum += + int(num/i)

    return sum

def is_abundant(num:int):
    return True if sum_of_proper_divisors(num)> num else False


def count_chain(n:int):
    if n<1:
        return None
    count=0
    while n!=1:
        if n%2==0:
            n=n/2
        elif n%2!=0:
            n=(3*n)+1
        count+=1
    count+=1

    return count
    

def print_grid(grid:list):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=' ')
        print('', end='\n')


def grid_move_right(position:list):
    position[1]+=1
    return 

def grid_move_down(position:list):
    position[0]+=1

def grid_move_left(position:list):
    position[1]-=1

def grid_move_up(position:list):
    position[0]-=1

def is_grid_complete(grid):
    for row in grid:
        if None in row:
            return False
    else:
        return True
def set_grid_at_position(grid:list,position:list, num:int):
    if(not is_grid_complete(grid)):
        grid[position[0]][position[1]] = num


def is_pandigital(num:int):
    str_num = str(num)
    return True if len(set(str_num)) == len(str_num) and '0' not in str_num else False

    

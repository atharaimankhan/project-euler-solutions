"""
Problem 28

URL: https://projecteuler.net/problem=28

"""


from utils import print_timed, grid_move_down, grid_move_left, grid_move_right, grid_move_up , print_grid, set_grid_at_position


def problem28():

    grid_number = 1001
    grid = [[None]*grid_number for i in range(grid_number)]
    center_of_grid = grid_number//2
    grid[center_of_grid][center_of_grid] = 1
    position = [center_of_grid,center_of_grid]
    steps=1
    i=1


    while None in grid[0]:
        if steps%2!=0:
            for s in range(steps):
                grid_move_right(position)
                i+=1
                set_grid_at_position(grid,position,i)
            for s in range(steps):
                grid_move_down(position)
                i+=1
                set_grid_at_position(grid,position,i)

        else:
            for s in range(steps):
                grid_move_left(position)
                i+=1
                set_grid_at_position(grid,position,i)
            for s in range(steps):
                grid_move_up(position)
                i+=1
                set_grid_at_position(grid,position,i)
        steps+=1    

    sum =0
    for i in range(grid_number):
        sum += grid[i][i]
    for i in range(1,center_of_grid+1):
        sum += grid[center_of_grid-i][center_of_grid+i]
        sum += grid[center_of_grid+i][center_of_grid-i]
        
    return sum

if __name__ == '__main__':
    
    print_timed(problem28)

import numpy as np

def isPossible(grid,x,y,n):
    for i in range(9):
        if  grid[x][i]==n or grid[i][y]==n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[x0+i][y0+j]==n:
                return False
    return True

def solver(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find
        for i in range(1,10):
            if isPossible(grid,row,col,i):
                grid[row][col] = i
                if solver(grid):
                    return True
                grid[row][col] = 0 
    return False



def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)  # row, col

    return None

print


    



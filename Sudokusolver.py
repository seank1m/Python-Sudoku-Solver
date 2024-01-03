import numpy as np

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,0,0]]

def possible(row,column,number):

    for i in range (0,9):
        if puzzle[row][i] == number:
            return False 

    for i in range (0,9):
        if puzzle[i][column] == number:
            return False
        
    x0 = (column // 3) * 3 
    y0 = (row // 3) * 3
    for i in range (0,3): 
        for j in range (0,3):
            if puzzle[y0+i][x0+j] == number:
                return False 
        
    return True 

def solver(): 
    global puzzle
    for row in range (0,9):
        for column in range (0,9):
            if puzzle[row][column] == 0:
                for number in range (1,10): 
                    if possible(row,column,number):
                        puzzle[row][column] = number
                        solver()
                        puzzle[row][column] = 0
                return

    print(np.matrix(puzzle))
    #Generate more solutions for the puzzle 
     
    input ('More possible solutions')

solver()
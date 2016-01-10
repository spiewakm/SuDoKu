"""
modul: 
generacja pelnego sudoku, na podstawie jednego danego ukladu, nastepnie
generacja usuwanie elementow zgodnie z danym poziomem
"""
import numpy as np

def createFullSudoku():
    """
    funkcja do tworzenia pełnej siatki Sudoku
    permutujemy podana siatke s
    """

    s = np.array([[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9,1],
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]])

    #Permute the rows 1-3, 4-6, or 7-9.
    row_per = np.concatenate([np.random.permutation(x) for x  in  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]])
    s = s[row_per, :]
    #Permute the columns 1-3, 4-6, or 7-9.

    col_per = np.concatenate([np.random.permutation(x) for x  in  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]])
    s = s[:, col_per]

    #Permute the 3x9 blocks of rows.

    block_row_per = np.concatenate(np.random.permutation([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
    s = s[block_row_per, :]

    #Permute the 9x3 blocks of columns.

    block_col_per = np.concatenate(np.random.permutation([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
    s = s[block_col_per, :]

    #Rotate the grid 90, 180, or 270 degrees.

    s = np.rot90(s, k = np.random.choice([1, 2, 3]))

    #Reflect the grid about the horizontal, vertical, or either diagonal axis.

    axis = np.random.choice(np.array(['h', 'v', 'd']))
    x = np.linspace(8, 0, 9, dtype= np.int16)

    if axis == 'h':
        s = s[x, :]
    elif axis == 'v':
        s = s[:, x]
    elif axis == 'd':
        s = s.T
    
    return s

def createSudoku(fullSudoku, level = 0):
    """
    funkcja do tworzenia sudoku do rozwiazania
    
    level:
    0: Begin
    1: Easy
    2: Medium
    3: Hard
    """

    g = fullSudoku.copy()

    for i in range(9):
        if all(g[i, :] != 0):
            x = np.random.choice(np.linspace(0, 8, 9, dtype = np.int16))
            g[i][x] = 0

        for j in range(9):
            if all(g[:, j] != 0):
                y = np.random.choice(np.linspace(0, 8, 9, dtype = np.int16))
                g[x][j] = 0

    if level >= 1:
        for i in range(3):
            for j in range(3):
                if any([any(x != 0) for x in g[3*i:(3*i+3), 3*j:(3*j+3)]]):
                    while(1):
                        x = np.random.choice(np.linspace(3*i, (3*i+2), 3, dtype = np.int16))
                        y = np.random.choice(np.linspace(3*j, (3*j+2), 3, dtype = np.int16))
                        if g[x, y] == 0: next
                        else:
                            g[x, y] = 0
                            break
        if level >= 2:
            add = 7
            while(add > 0):
                x = np.random.choice(np.linspace(0, 8, 9, dtype = np.int16))
                y = np.random.choice(np.linspace(0, 8, 9, dtype = np.int16))
                if g[x, y] == 0: next
                else:
                    g[x, y] = 0
                    add -= 1

            if level == 3:
                add = 14
                while(add > 0):
                    x = np.random.choice(np.linspace(0, 8, 9, dtype = np.int16))
                    y = np.random.choice(np.linspace(0, 8, 9, dtype = np.int16))
                    if g[x, y] == 0: next
                    else:
                        g[x, y] = 0
                        add -= 1
                        
    return g

#createSudoku(level = 3)
import numpy as np
import matplotlib.pyplot as plt

grid = np.random.randint(low=0, high=2, size=(20, 20))

print(grid)

def safe_get(grid, i, j):
    try:
        return grid[i][j]
    except IndexError:
        return 0

def countAlive(i, j, grid):
    count = 0
    adjs = [safe_get(grid, i-1, j),
            safe_get(grid, i+1, j),
            safe_get(grid, i, j-1),
            safe_get(grid, i, j+1)]

    for i in range(4):
        if(adjs[i] == 1):
            count += 1
    return count

def gen(old):
    new = old
    # super inefficent
    for i in range(len(old)):
        for j in range(len(old[i])):
            n = countAlive(i, j, old)
            if (old[i][j] == 1):
                if (n >= 3):
                    new[i][j] = 0
                else:
                    new[i][j] = 1
            else:
                if (n > 2):
                    new[i][j] = 1
                else:
                    new[i][j] = 0
    return new



for i in range(10):
    new_grid = gen(grid)
    plt.imshow(new_grid)
    plt.show()
    grid = new_grid

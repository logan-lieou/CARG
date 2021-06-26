import numpy as np
import matplotlib.pyplot as plt

grid = np.random.randint(low=0, high=2, size=(20, 20))

print(grid)

def countAlive(i, j, grid):
    try:
        adjs = [grid[i-1][j],
            grid[i+1][j],
            grid[i][j-1],
            grid[i][j+1]]
    except IndexError:
        adjs = [0,
                0,
                0,
                0]

    # computationally less efficent than range(4)
    count = 0
    # need to catch error lol
    for i in range(len(adjs)):
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

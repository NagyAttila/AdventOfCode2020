input_ = """...#...#
#######.
....###.
.#..#...
#.#.....
.##.....
#.####..
#....##."""

# input_ = """.#.
# ..#
# ###"""

input_ = """...
###
..."""

import itertools
import numpy as np
from copy import deepcopy

def getCombinations():
    x = [-1, 0, +1]
    xs = [p for p in itertools.product(x, repeat=3)]
    xs.remove((0,0,0))
    return xs

def isValid(xs,z,y,x):
    sz = len(xs)
    sy = len(xs[0])
    sx = len(xs[0][0])
    return z>0 and y>0 and x>0 and z<sz and y<sy and x<sx

def countNeighbour(xs, z, y, x):
    cmbs = getCombinations()
    count = 0
    for cmb in cmbs:
        x_,y_,z_ = cmb
        if isValid(xs,z+z_,y+y_,x+x_) and xs[z+z_][y+y_][x+x_] == '#':
            count += 1
    return count

def printWorld(xs):
    for i,z in enumerate(xs):
        print('z:',i)
        for y in z:
            for x in y:
                print(x,end='')
            print('')

def initWorld(xs):
    size_x = len(xs) + 2
    size_y = len(xs[0]) + 2
    size_z = len(xs[0][0]) + 2
    nxs = [[['.' for _ in range(size_z)] for _ in range(size_y)] for _ in range(size_x)]
    for x in range(1,size_x-1):
        for y in range(1,size_y-1):
            for z in range(1,size_z-1):
                print(xs,x,y,z)
                nxs[x][y][z] = xs[x-1][y-1][z-1][0]
    return np.transpose(nxs, (2, 0,1))

def expandWorld(xs):
    size_z = len(xs) + 2
    size_y = len(xs[0]) + 2
    size_x = len(xs[0][0]) + 2
    nxs = [[['.' for _ in range(size_x)] for _ in range(size_y)] for _ in range(size_z)]
    for z in range(1,size_z-1):
        for y in range(1,size_y-1):
            for x in range(1,size_x-1):
                nxs[z][y][x] = xs[z-1][y-1][x-1]
    return nxs

xs = input_.split('\n')
xs = list(map(list, xs))

for i in range(6):
    if i==0:
        nxs = initWorld(xs)
    else:
        nxs = expandWorld(xs)

    xs = deepcopy(nxs)
    size_z = len(xs)
    size_y = len(xs[0])
    size_x = len(xs[0][0])
    for z in range(size_z):
        for y in range(size_y):
            for x in range(size_x):
                e = xs[z][y][x]
                n = countNeighbour(xs,z,y,x)
                if e == '.' and n == 3:
                    nxs[z][y][x] = '#'
                elif e == '#' and not (n == 3 or n == 2):
                    nxs[z][y][x] = '.'
    xs = deepcopy(nxs)
    # printWorld( nxs)

solution = 0
for z in range(size_z):
    for y in range(size_y):
        for x in range(size_x):
            e = xs[z][y][x]
            if e == '#':
                solution += 1

print("Part #1:", solution)

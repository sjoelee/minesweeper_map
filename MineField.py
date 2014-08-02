from __future__ import print_function
import fileinput

class MineField():
    def process(data):
        print(data)
        return

    def getNumMines(x, y):
        # Check to see if there's a mine at location (x,y)
        if mineXArray[x] != 0:
            if str(y) in mineXArray[x]:
                return -1
    
        numMines = 0
        numMines += getNumMinesColumn(x-1, y)
        numMines += getNumMinesColumn(x, y)
        numMines += getNumMinesColumn(x+1, y)
    
        return numMines
    
    def getNumMinesColumn(x, y):
        numMines = 0
    
        if x < 0 or x >= gridSize[1]:
            return numMines
    
        if mineXArray[x] == 0: # No mines on column x
            return numMines
    
        if str(y-1) in mineXArray[x]:
            numMines += 1
        if str(y) in mineXArray[x]:
            numMines += 1
        if str(y+1) in mineXArray[x]:
            numMines += 1
    
        return numMines
    
    def printMineMap():
        for y in xrange(gridSize[0]): #rows
            for x in xrange(gridSize[1]): #columns
                numMines = getNumMines(x, y)
                if numMines == -1:
                    print("X", end=' ')
                else:
                    print(str(numMines), end=' ')
            print('')
    
    # Store the mine locations within an array of dictionaries
    # gridSize = (# rows, #cols)
    with open('test.txt') as f:
        gridSize = map(int, f.readline().split('x'))
        mineXArray = [0] * gridSize[1]
        for line in f:
            x, y = map(int, line.split(','))
            if mineXArray[x] == 0:
                mineXArray[x] = {str(y): True}
            else:
                mineXArray[x][str(y)] = True
    
    #printMineMap()
    

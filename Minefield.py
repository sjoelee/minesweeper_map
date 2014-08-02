from __future__ import print_function
class Minefield():
    @staticmethod
    def process(data):
        if not data:
            return ''
        dataSplit = data.split('\n')
        gridSize = map(int, dataSplit[0].split('x'))
        mineXArray = [0] * gridSize[1]
        for line in dataSplit[1:-1]:
            x, y = map(int, line.split(','))
            if mineXArray[x] == 0:
                mineXArray[x] = {str(y): True}
            else:
                mineXArray[x][str(y)] = True

        Minefield.printMineMap(gridSize, mineXArray)
        return

    @staticmethod
    def getNumMines(gridSize, x, y, mineXArray):
        # Check to see if there's a mine at location (x,y)
        if mineXArray[x] != 0:
            if str(y) in mineXArray[x]:
                return -1
    
        numMines = 0
        numMines += Minefield.getNumMinesColumn(gridSize, x-1, y, mineXArray)
        numMines += Minefield.getNumMinesColumn(gridSize, x, y, mineXArray)
        numMines += Minefield.getNumMinesColumn(gridSize, x+1, y, mineXArray)
    
        return numMines

    @staticmethod    
    def getNumMinesColumn(gridSize, x, y, mineXArray):
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

    @staticmethod
    def printMineMap(gridSize, mineXArray):
        if (0,0) == gridSize:
            print('')
        for y in xrange(gridSize[0]): #rows
            for x in xrange(gridSize[1]): #columns
                numMines = Minefield.getNumMines(gridSize, x, y, mineXArray)
                if numMines == -1:
                    print("X", end=' ')
                else:
                    print(str(numMines), end=' ')
            print('')

   
    # Store the mine locations within an array of dictionaries
    # gridSize = (# rows, #cols)
    # with open('test.txt') as f:
    #     gridSize = map(int, f.readline().split('x'))
    #     mineXArray = [0] * gridSize[1]
    #     for line in f:
    #         x, y = map(int, line.split(','))
    #         if mineXArray[x] == 0:
    #             mineXArray[x] = {str(y): True}
    #         else:
    #             mineXArray[x][str(y)] = True
    
    #printMineMap()
    

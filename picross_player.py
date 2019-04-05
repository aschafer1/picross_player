class Board:
    def __init__(self, boardSizeX, boardSizeY):
        self.boardSizeX = boardSizeX
        self.boardSizeY = boardSizeY
        #self.numberArray = numberArray
        self.boardArray[self.boardSizeX][self.boardSizeY]
        for y in range(self.boardSizeY):
            for x in range(self.boardSizeX):
                self.boardArray[x][y] = 0


    def printBoard(self):
            for y in range(self.boardSizeY):
                print("-")
                for x in range(self.boardSizeX):
                    print("|")
                    if self.boardArray[x][y] == 0:
                        print(" ")
                    elif self.boardArray[x][y] == 1:
                        print("X")
                    else :
                        print("#")
                    print("|")

                print("-")

b = Board(10,10)
b.printBoard()
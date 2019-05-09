class Board:
    def __init__(self, boardSizeX, boardSizeY):
        self.boardSizeX = boardSizeX
        self.boardSizeY = boardSizeY
        self.boardArray = [[0] * self.boardSizeY] * self.boardSizeX



    def printBoard(self):

        print(self.boardArray)
        for y in range(self.boardSizeY):
                for x in range(self.boardSizeX):
                    print("|", end="")
                    if self.boardArray[x][y] == 0:
                        print(" ", end="")
                    elif self.boardArray[x][y] == 1:
                        print("X", end="")
                    else :
                        print("#", end="")
                print("|")
                
                for i in range((self.boardSizeX * 2) + 1):
                    print("-", end="")
                print("")

b = Board(10,10)
b.printBoard()
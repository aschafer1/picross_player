
class Board:
    def __init__(self, boardSizeX, boardSizeY):
        self.empty = 0
        self.filled = 1
        self.marked = 2
        self.boardSizeX = boardSizeX
        self.boardSizeY = boardSizeY
        self.boardArray = [[0 for i in range(self.boardSizeX)] for j in range(self.boardSizeY)]




    def printBoard(self):
        for i in range((self.boardSizeX * 2) + 1):
            print("-", end="")
        print("")
        for y in range(self.boardSizeY):
                for x in range(self.boardSizeX):
                    print("|", end="")
                    if self.boardArray[x][y] == self.empty:
                        print(" ", end="")
                    elif self.boardArray[x][y] == self.filled:
                        print("X", end="")
                    else :
                        print("#", end="")
                print("|")
                
                for i in range((self.boardSizeX * 2) + 1):
                    print("-", end="")
                print("")
    
                
    def fillIn(self,x,y):
        self.boardArray[x][y] = self.filled




b = Board(10,10)
b.printBoard()

print("\n\n")
b.fillIn(2,0)
b.printBoard()
#class to run the board itself, player will be built to use this eventually
class Board:
    #initilizes values for different square states, board sizes and initilizes the board array
    def __init__(self, boardSizeX, boardSizeY):
        self.empty = 0
        self.filled = 1
        self.marked = 2
        self.boardSizeX = boardSizeX
        self.boardSizeY = boardSizeY
        self.boardArray = [[0 for i in range(self.boardSizeX)] for j in range(self.boardSizeY)]



    #prints the full board with X for the marked squares and # for the filled in squares and a space for empty spaces
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
                        print("#", end="")
                    else :
                        print("X", end="")
                print("|")
                
                for i in range((self.boardSizeX * 2) + 1):
                    print("-", end="")
                print("")
    
    # x is the x coordinate of the square to fill in, y is y coordinate. fills in the indicated square            
    def fillSquare(self,x,y):
        self.boardArray[x][y] = self.filled
    # x is the x coordinate of the square to mark, y is y coordinate. marks the indicated square
    def markSquare(self,x,y):
        self.boardArray[x][y] = self.marked
    # x is the x coordinate of the square to empty, y is y coordinate. Empties the indicated square
    def emptySquare(self,x,y):
        self.boardArray[x][y] = self.empty

    def does_number_overlap(self,number,space):
        if space <= 2:
            return number == space
        else:
            return number > (space/2)

    def num_can_be_filled(self,number,space):
        if space <=2:
            if number == space:
                return number
            else:
                return 0
        else:
            if number > space/2:
                return 2*(number -(space/2))
            else:
                return 0
        

#testing code
b = Board(10,10)
b.printBoard()

print("\n\n")
b.fillSquare(2,0)
b.printBoard()
b.markSquare(3,0)
b.printBoard()
b.emptySquare(2,0)
b.emptySquare(3,0)
b.printBoard()

print(b.does_number_overlap(50,97))
print(b.does_number_overlap(49,97))
print(b.num_can_be_filled(5,10))
print(b.num_can_be_filled(6,10))
print(b.num_can_be_filled(7,10))
print(b.num_can_be_filled(8,10))
print(b.num_can_be_filled(9,10))
print(b.num_can_be_filled(10,10))

print("")
print(b.num_can_be_filled(5,9))
print(b.num_can_be_filled(6,9))
print(b.num_can_be_filled(7,9))

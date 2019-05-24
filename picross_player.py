#
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
        #tuple with first entry being a list of lists that each of the sub-lists is the clues for that respecitve vertical column, corresponding to 
        #their x coordinates
        self.clues = ([],[])

    #adds clues, allows user to add the clues to the board manually, where self.clues(x,y) is a tuple where x is a list of clues for each vertical column,
    # left to right and y is a list of clues for each row, top to bottom
    # y is not implemented yet
    def add_clues(self):
        print( "enter one number at a time, press enter without typing to finish the clue for a line")
        self.clues 
        for x in range(self.boardSizeX):
            self.clues[0].append([])
            print("enter clues for column: " + str(x) )
            clue = "test"
            while True:
                clue = input("Enter clue:")
                if clue == "":
                    break
                clue = int(clue,10)
                self.clues[0][x].append(clue)

        print(self.clues)

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

    # number is the size of the clue, space is the size of the cells
    # This returns a bool on whether a certain clue can be filled out, based on the simple boxes method
    def does_number_overlap(self,number,space):
        if space <= 2:
            return number == space
        else:
            return number > (space/2)


    #number is the size of clue, space is the size of the group of cells it is in
    #returns the number of cells that can be filled in using the simple boxes method on a single number clue
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
    
    #def reason_line(self):
        

def test():
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
    b.add_clues()

test()

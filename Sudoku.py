
def areLegalValues(values):
    # check if values is a list
    if type(values) != list: return False
    # check if the list is empty
    if len(values) ==0: return False
    # check if it's in correct dimension n**2
    if (len(values)**0.5)%1 != 0: return False
    # check if it's all integers
    try:
        for i in values:
            if i%1 !=0:
                return False
    except TypeError: return False
    # check if numbers are in range
    if max(values)>len(values) or min(values) < 0: return False
    # check if there are duplicates
    for legalNumbers in range(1, len(values)+1):
        if values.count(legalNumbers) > 1: return False
    return True

def isLegalRow(board, row):
    # check if the row number is in range
    if row<0 or row > len(board)-1: return False
    # create a 1D list
    myRow = copy.copy(board[row])
    # check if every value in row are legal
    return areLegalValues(myRow)

def isLegalCol(myBoard, col):
    board = copy.deepcopy(myBoard)
    try:
        # create a 1D list
        myCol = [board[i][col] for i in range(len(board))]
        return areLegalValues(myCol)
    # return false if index out of range
    except IndexError: return False

def isLegalBlock(board, block):
    n = int(len(board)**0.5)
    # check if block is in proper range
    if block+1 > n**2 or block+1 <= 0: return False
    # find the x,y position of the top left element of the desired block
    xPos = (block % n) * n
    yPos = (block // n) * n
    lst = []
    # add elements into new list
    for row in range(yPos, yPos+n):
        for col in range(xPos, xPos+n):
            lst.append((board[row][col]))
    # check if block is legal
    return areLegalValues(lst)

def isLegalSudoku(board):
    n = int(len(board))  # dimension of the board n*n
    for row in range(n):  # check every row
        if not isLegalRow(board, row):
            return False
    for col in range(n):  # check every column
        if not isLegalCol(board, col):
            return False
    for block in range(n):  # check every block
        if not isLegalBlock(board, block):
            return False
    return True

######################################################################
# GRAPHICS/ANIMATION PROBLEMS
# ignore_rest
# The autograder will ignore all code below here
# (But we won't!  This is where all tkinter problems go!)
######################################################################

#### #4: Sudoku Animation ####

from tkinter import *
def starterBoard():
    board1 =[[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [5, 0, 8, 1, 3, 9, 6, 2, 4],
             [4, 9, 6, 8, 7, 2, 1, 5, 3],
             [9, 5, 2, 3, 8, 1, 4, 6, 7],
             [6, 4, 1, 2, 9, 7, 8, 3, 5],
             [3, 8, 7, 5, 6, 4, 0, 9, 1],
             [7, 1, 9, 6, 2, 3, 5, 4, 8],
             [8, 6, 4, 9, 1, 5, 3, 7, 2],
             [2, 3, 5, 7, 4, 8, 9, 1, 6]]

    board2 =[[0, 2, 0, 4, 0, 6, 0, 0, 9],
             [5, 0, 8, 0, 3, 0, 6, 2, 4],
             [4, 0, 0, 8, 0, 0, 1, 0, 3],
             [0, 0, 2, 0, 0, 1, 0, 6, 0],
             [0, 0, 0, 2, 0, 0, 8, 0, 5],
             [0, 8, 0, 0, 0, 4, 0, 9, 1],
             [7, 0, 9, 0, 0, 3, 0, 4, 0],
             [0, 6, 0, 9, 1, 0, 3, 0, 2],
             [2, 3, 5, 0, 0, 0, 0, 1, 0]]
    return board1

def init(data):
    data.board = starterBoard()
    data.dimension = len(data.board)
    data.n = int(data.dimension**0.5)
    data.cellSize = min(data.width, data.height)//data.dimension
    data.initialPos = []  # list of positions of initial values
    for row in range(data.dimension):
        for col in range(data.dimension):
            if data.board[row][col] != 0:
                data.initialPos.append((row, col))
    data.currentX, data.currentY = 0, 0     # current cell position
    data.finished = False

def mousePressed(event, data):
    # disable mouse pressing when finished
    if data.finished: return None
    row = event.y // data.cellSize
    col = event.x // data.cellSize
    # change current highlighted cell only when click inside the playground
    if 0 <= row <= data.dimension-1 and 0<= col <= data.dimension-1:
        data.currentX, data.currentY = col, row

def keyPressed(event, data):
    import string
    import copy
    # disable key pressing when finished
    if data.finished: return None
    if event.char in string.digits:
        testBoard = copy.deepcopy(data.board)
        testBoard[data.currentY][data.currentX] = int(event.char)
        # do not update number if it leads to an illegal sudoku
        if isLegalSudoku(testBoard):
            # change current number only when the number is not givens initially
            if (data.currentY, data.currentX) not in data.initialPos:
                data.board[data.currentY][data.currentX] = int(event.char)
        else:
            print("Sorry, you are not allowed to do this!")
    # move and wrap around with arrow keys
    elif event.keysym == "Up":
        data.currentY = (data.currentY - 1) % data.dimension
    elif event.keysym == "Down":
        data.currentY = (data.currentY + 1) % data.dimension
    elif event.keysym == "Right":
        data.currentX = (data.currentX + 1) % data.dimension
    elif event.keysym == "Left":
        data.currentX = (data.currentX - 1) % data.dimension
    # allow user to delete a user-input
    elif event.keysym == "BackSpace":
        if (data.currentY, data.currentX) not in data.initialPos:
            data.board[data.currentY][data.currentX] = 0

def drawBoxes(canvas, data):
    size = data.cellSize
    # draw all boxes
    for row in range(data.dimension):
        for col in range(data.dimension):
            canvas.create_rectangle(col*size, row*size,
                                    col*size + data.cellSize, row*size + data.cellSize)
    # draw current highlighted box
    canvas.create_rectangle(data.currentX*size, data.currentY*size,
                            data.currentX*size + data.cellSize,
                            data.currentY*size + data.cellSize,
                            fill = "yellow"
                            )
    for cols in range(0, data.dimension + 1, data.n):
        canvas.create_line(cols*data.cellSize, 0, cols*data.cellSize, data.dimension*data.cellSize, width=5)
    for rows in range(0, data.dimension + 1, data.n):
        canvas.create_line(0, rows*data.cellSize, data.dimension*data.cellSize, rows*data.cellSize, width=5)

def drawNumbers(canvas, data): # draw all the numbers on the board
    size = data.cellSize
    for row in range(data.dimension):
        for col in range(data.dimension):
            # draw initial given values
            if (row,col) in data.initialPos:
                canvas.create_text(col*size+size/2, row*size+size/2,
                                   text = str(data.board[row][col]),
                                   fill="darkBlue",
                                   font="Times 23 bold")
            # draw user-input values
            elif data.board[row][col] != 0:
                canvas.create_text(col * size + size / 2, row * size + size / 2,
                                   text=str(data.board[row][col]),
                                   fill="red",
                                   font="Times 23 bold")

def isfinished(data): # check if the board is complete
    for row in range(data.dimension):
        for col in range(data.dimension): # finished when no cell is 0
            if data.board[row][col] == 0:
                return False
    return True

def redrawAll(canvas, data):
    drawBoxes(canvas,data)
    drawNumbers(canvas, data)
    if isfinished(data):  # escape when finished
        data.finished = True
        # draw some nice messages to congrats the user
        canvas.create_rectangle(0, 2*data.height/5, data.width, 3*data.height/5, fill="green")
        canvas.create_text(data.width/2, data.height/2,
                           text="You Won!",
                           fill="purple",
                           font="blue 26 bold underline")

def runSudoku(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed


def testSudokuAnimation():
    print("Running Sudoku Animation...", end="")
    # board1
    #runSudoku(500, 500)
    runSudoku(700, 500)
    print("Done!")

testSudokuAnimation()
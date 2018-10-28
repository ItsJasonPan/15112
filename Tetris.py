# Updated Animation Starter Code

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.rows, data.cols, data.cellSize, data.margin = gameDimensions()
    # empty board is all blue
    data.board = [["blue"] * data.cols for i in range(data.rows)]
    newFallingPiece(data)
    data.score = 0
    data.gameover = False


def mousePressed(event, data):
    # this game does not need mouse
    pass


def keyPressed(event, data):
    import copy
    if not data.gameover:
        if event.char == "s":
            newFallingPiece(data)
        # move down, left or right when movable
        if event.keysym == "Down":
            if fallingPieceIsLegal(data, 1, 0):
                moveFallingPiece(data, 1, 0)
        if event.keysym == "Left":
            if fallingPieceIsLegal(data, 0, -1):
                moveFallingPiece(data, 0, -1)
        if event.keysym == "Right":
            if fallingPieceIsLegal(data, 0, 1):
                moveFallingPiece(data, 0, 1)
        # rotate when nothing is blocking
        if event.keysym == "Up":
            temp = copy.deepcopy(data.fallingPiece[0])
            tempStorage = data.fallingPieceRow, data.fallingPieceCol
            rotateFallingPiece(data)
            # restore to original orientation when the rotation is illegal
            if not fallingPieceIsLegal(data, 0, 0):
                data.fallingPiece = temp, data.fallingPiece[1]
                data.fallingPieceRow, data.fallingPieceCol = tempStorage


def timerFired(data):
    if not data.gameover:
        # move the falling piece down by one block when movable
        if fallingPieceIsLegal(data, 1, 0):
            moveFallingPiece(data, 1, 0)
        else:
            # place falling piece when not movable
            placeFallingPiece(data)


def drawCell(row, col, color, canvas, data):
    canvas.create_rectangle(col * data.cellSize + data.margin,
                            row * data.cellSize + data.margin,
                            (col + 1) * data.cellSize + data.margin,
                            (row + 1) * data.cellSize + data.margin,
                            fill=color, width=3)


def drawBoard(canvas, data):
    # draw the entire board cell by cell
    for row in range(data.rows):
        for col in range(data.cols):
            color = data.board[row][col]
            drawCell(row, col,color, canvas, data)


def tetrisPiece(data):
    # 7 types of tetris piece
    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]
    data.tetrisPieces = [iPiece, jPiece, lPiece, oPiece,
                         sPiece, tPiece, zPiece]
    # each piece corresponds to a specific color
    data.tetrisPieceColors = ["red", "yellow", "magenta",
                              "pink", "cyan", "green", "orange"]


def newFallingPiece(data):
    tetrisPiece(data)
    import random
    # choose a random shape for the new piece
    randomIndex = random.randint(0, len(data.tetrisPieces) - 1)
    data.fallingPiece = (data.tetrisPieces[randomIndex],
                         data.tetrisPieceColors[randomIndex])
    # row location of the top left piece
    data.fallingPieceRow = 0
    numFallingPieceCols = len(data.fallingPiece[0][0])
    # column location of the top left piece
    data.fallingPieceCol = len(data.board[0]) // 2 - numFallingPieceCols//2
    # test if it's game over
    for row in range(len(data.fallingPiece[0])):
        for col in range(len(data.fallingPiece[0][0])):
            if data.fallingPiece[0][row][col]:
                # game over when the spawn area are not all empty
                r, c = data.fallingPieceRow, data.fallingPieceCol
                if data.board[row + r][col + c] != "blue":
                    data.gameover = True


def drawFallingPiece(canvas, data):
    # draw falling piece cell by cell
    for row in range(len(data.fallingPiece[0])):
        for col in range(len(data.fallingPiece[0][0])):
            if data.fallingPiece[0][row][col]:
                color = data.fallingPiece[1]
                drawCell(row + data.fallingPieceRow,
                         col + data.fallingPieceCol,
                         color, canvas, data)


def moveFallingPiece(data, drow, dcol):
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol


def fallingPieceIsLegal(data, drow, dcol):
    for row in range(len(data.fallingPiece[0])):
        for col in range(len(data.fallingPiece[0][0])):
            if data.fallingPiece[0][row][col]:
                nextRow = data.fallingPieceRow + row + drow
                nextCol = data.fallingPieceCol + col + dcol
                if nextRow > data.rows-1 or nextCol > data.cols-1\
                        or nextCol < 0:
                    return False
                elif data.board[nextRow][nextCol] != "blue":
                    return False
    return True


def rotateFallingPiece(data):
    myPiece = data.fallingPiece[0]
    newPiece = [[None] * len(myPiece) for i in range(len(myPiece[0]))]
    # rotate the original piece counterclockwise 90 degrees
    for row in range(len(newPiece)):
        for col in range(len(newPiece[0])):
            newPiece[row][col] = myPiece[col][len(myPiece[0])-1-row]
    # update the location and shape of the original falling piece
    newRow = data.fallingPieceRow + int(len(myPiece) / 2 - len(myPiece[0]) / 2)
    newCol = data.fallingPieceCol + int(len(myPiece[0]) / 2 - len(myPiece) / 2)
    data.fallingPiece = (newPiece, data.fallingPiece[1])
    data.fallingPieceRow = newRow
    data.fallingPieceCol = newCol


def placeFallingPiece(data):
    piece, color = data.fallingPiece
    for row in range(len(piece)):
        for col in range(len(piece[0])):
            if piece[row][col] == True:
                # place color on the original board when
                # the falling piece is interrupted
                rowBoard = row + data.fallingPieceRow
                colBoard = col + data.fallingPieceCol
                data.board[rowBoard][colBoard] = color
    # generate a new falling piece
    newFallingPiece(data)
    # check if any rows can be removed
    removeFullRows(data)


def removeFullRows(data):
    totalRemoved = 0
    for row in range(len(data.board)):
        if "blue" not in data.board[row]:
            data.board.pop(row)
            # remove rows when it's completely full
            data.board.insert(0, ["blue"] * data.cols)
            totalRemoved += 1
    # total score will be # of lines removed square
    data.score += totalRemoved ** 2


def drawScore(canvas, data):
    canvas.create_text(data.width/2, 15, text=("Score:", data.score),
                       fill="dark blue", font="30")


def drawGameOver(canvas, data):
    # draw text and background when game over
    canvas.create_rectangle(data.margin, data.height * 2/5,
                            data.width - data.margin, data.height/2,
                            fill="maroon")
    canvas.create_text(data.width/2, data.height/2, text="Game Over!",
                       fill="white", font="Chalkduster 28 bold", anchor=S)


def redrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="orange")
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)
    drawScore(canvas, data)
    if data.gameover:
        drawGameOver(canvas, data)


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
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

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 200 # milliseconds
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
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


def gameDimensions():
    # preset the dimension
    rows = 25
    cols = 13
    cellSize = 30
    margin = 40
    return rows, cols, cellSize, margin


def playTetris():
    rows, cols, cellSize, margin = gameDimensions()
    # calculate the board size and start the game!
    height = rows * cellSize + 2 * margin
    width = cols * cellSize + 2 * margin
    run(width, height)


playTetris()

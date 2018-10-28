
from tkinter import *

# land = 0, wall = 1, box = 2, storage =3, finished = 4, man = 5, man on storage =6
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def starterBoardSokoban():
    # land = 0, wall = 1, box = 2, storage =3, finished = 4, man = 5, man on storage =6
    #please use 700,850 for dimension
    # map 1 difficulty level 2/10
    mymap1 =[[0, 0, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 0, 0, 0, 1, 0],
             [1, 3, 5, 2, 0, 0, 1, 0],
             [1, 1, 1, 0, 2, 3, 1, 0],
             [1, 3, 1, 1, 2, 0, 1, 0],
             [1, 0, 1, 0, 3, 0, 1, 1],
             [1, 2, 0, 4, 2, 2, 3, 1],
             [1, 0, 0, 0, 3, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]
    # please use 1000,600 for dimension
    # map 3 difficulty level 5/10
    mymap2 =[[0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,1,1,1,0,0,2,1,1,0,0,0,0,0,0,0,0,0,0],
             [0,0,1,0,0,2,0,2,0,1,0,0,0,0,0,0,0,0,0,0],
             [1,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1],
             [1,0,0,0,1,0,1,1,0,1,1,1,1,1,0,0,0,3,3,1],
             [1,0,2,0,0,2,0,0,0,0,0,0,0,0,0,0,0,3,3,1],
             [1,1,1,1,1,0,1,1,1,0,1,5,1,1,0,0,0,3,3,1],
             [0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
             [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]]
    # please use 1000 780 for dimension
    # map 3 difficulty level 8/10
    mymap3 =[[1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
            [1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0],
            [1,0,1,0,1,1,1,1,1,1,2,0,0,0,0,0,1,0],
            [1,0,1,0,1,0,0,0,0,1,0,1,3,1,0,0,1,0],
            [1,0,1,0,1,0,2,0,0,2,0,3,5,3,0,0,1,0],
            [1,0,1,0,1,0,0,2,0,1,0,1,3,1,0,0,1,1],
            [1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1],
            [1,0,1,0,1,1,1,1,1,1,0,0,0,1,0,0,1,1],
            [1,0,1,0,0,0,0,3,0,0,2,0,0,0,2,0,1,0],
            [1,0,1,1,1,1,1,0,1,1,3,1,1,1,3,1,1,1],
            [1,0,2,0,0,0,2,0,1,0,0,0,0,3,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    return mymap3



def initSokoban(data):
    import copy
    data.board = starterBoardSokoban()
    data.originalBoard = copy.deepcopy(data.board)
    data.dimensionR = len(data.board)
    data.dimensionC = len(data.board[0])
    data.size = data.cellSize = min((data.width//data.dimensionC),
                                    (data.height//data.dimensionR))
    data.landPos = []
    data.wallPos = []
    data.boxPos = []
    data.stoPos = []
    data.finPos = []
    data.man = []
    # track the positions of land, wall, box, storage, finished box, man, and man on storage
    for row in range(data.dimensionR):
        for col in range(data.dimensionC):
            if data.board[row][col] == 0:
                data.landPos.append((row, col))
            elif data.board[row][col] == 1:
                data.wallPos.append((row, col))
            elif data.board[row][col] == 2:
                data.boxPos.append((row, col))
            elif data.board[row][col] == 3:
                data.stoPos.append((row, col))
            elif data.board[row][col] == 4:
                data.finPos.append((row, col))
            elif data.board[row][col] == 5 or data.board[row][col] == 6:
                data.man.append((row, col))
    data.currentR, data.currentC = data.man[0]

def updataAll(data):
    data.landPos = []
    data.wallPos = []
    data.boxPos = []
    data.stoPos = []
    data.finPos = []
    data.man = []
    # update the position of all elements
    for row in range(data.dimensionR):
        for col in range(data.dimensionC):
            if data.board[row][col] == 0:
                data.landPos.append((row, col))
            elif data.board[row][col] == 1:
                data.wallPos.append((row, col))
            elif data.board[row][col] == 2:
                data.boxPos.append((row, col))
            elif data.board[row][col] == 3:
                data.stoPos.append((row, col))
            elif data.board[row][col] == 4:
                data.finPos.append((row, col))
            elif data.board[row][col] == 5 or data.board[row][col] == 6:
                data.man.append((row, col))
    data.currentR, data.currentC = data.man[0]
    data.finished = False

def mousePressedSokoban(event, data):
    import copy
    # allow users to restart the game
    if data.width / 3 <= event.x <= 2 * data.width / 3 \
        and data.height - 50 <= event.y <= data.height:
        data.board = copy.deepcopy(data.originalBoard)

def keyPressedSokoban(event, data):
    # move only when the move is legal
    if data.finished: return None
    if event.keysym == "Up":
        if movable(data, 0, -1):
            move(data, 0, -1)
    elif event.keysym == "Down":
        if movable(data, 0, 1):
            move(data, 0, 1)
    elif event.keysym == "Right":
        if movable(data, 1, 0):
            move(data, 1, 0)
    elif event.keysym == "Left":
        if movable(data, -1, 0):
            move(data, -1, 0)

def move(data, x, y):
    next = data.board[data.currentR + y][data.currentC + x]
    # when next cell is land
    if next == 0:
        data.board[data.currentR + y][data.currentC + x] = 5
        if data.board[data.currentR][data.currentC] == 6:
            data.board[data.currentR][data.currentC] = 3
        else:
            data.board[data.currentR][data.currentC] = 0
    # when next cell is box
    elif next == 2:
        data.board[data.currentR + y][data.currentC + x] = 5
        if data.board[data.currentR + 2*y][data.currentC + 2*x] == 3:
            data.board[data.currentR + 2*y][data.currentC + 2*x] = 4
        else:
            data.board[data.currentR + 2 * y][data.currentC + 2 * x] =2
        if data.board[data.currentR][data.currentC] == 6:
            data.board[data.currentR][data.currentC] = 3
        else:
            data.board[data.currentR][data.currentC] = 0
    # when next cell is storage
    elif next == 3:
        data.board[data.currentR + y][data.currentC + x] = 6
        if data.board[data.currentR][data.currentC] == 6:
            data.board[data.currentR][data.currentC] = 3
        else:
            data.board[data.currentR][data.currentC] = 0
    # when next cell is finished box
    elif next == 4:
        data.board[data.currentR + y][data.currentC + x] = 6
        if data.board[data.currentR + 2 * y][data.currentC + 2 * x] == 3:
            data.board[data.currentR + 2 * y][data.currentC + 2 * x] = 4
        elif data.board[data.currentR + 2 * y][data.currentC + 2 * x] == 0:
            data.board[data.currentR + 2 * y][data.currentC + 2 * x] = 2
        if data.board[data.currentR][data.currentC] == 6:
            data.board[data.currentR][data.currentC] = 3
        else:
            data.board[data.currentR][data.currentC] = 0

def movable(data, x, y):  # check if the new move is legal
    if 0 <= data.currentC+ x < data.dimensionC and\
        0 <= data.currentR + y < data.dimensionR:
        next = data.board[data.currentR+y][data.currentC+x]
    else:
        return False
    # illegal if next cell is wall
    if next == 1:
        return False
    elif next == 2 or next ==4:
        # illegal if the cell after the next cell is a wall, a box, or a finished box
        if 0 <= data.currentC + 2*x < data.dimensionC and \
                0 <= data.currentR + 2*y < data.dimensionR:
            newNext = data.board[data.currentR+2*y][data.currentC+2*x]
        else:
            return False
        if newNext == 1 or newNext ==2 or newNext ==4: return False
    return True

def drawAll(canvas, data):
    size = data.cellSize
    # draw all cells
    for row in range(data.dimensionR):
        for col in range(data.dimensionC):
            canvas.create_rectangle(col*size, row*size,
                                    col*size + data.cellSize,
                                    row*size + data.cellSize,
                                    fill = "tan",
                                    outline = "tan")
            # following are not using if-else statement to avoid bugs when man on a storage
            # draw walls
            if (row, col) in data.wallPos:
                drawWall(canvas, data, row, col)
            # draw boxes
            if (row, col) in data.boxPos:
                boxColor = rgbString(216, 142, 55)
                drawBox(canvas, data, row, col,boxColor)
            # draw storage
            if (row, col) in data.stoPos or data.board[row][col]==6:
                shrink = size/3
                canvas.create_oval(col * size+shrink, row * size+shrink,
                                        col * size + data.cellSize-shrink,
                                        row * size + data.cellSize-shrink,
                                        fill="pink",
                                        outline="pink")
            # draw finished box
            if (row, col) in data.finPos:
                finboxColor = rgbString(124, 52, 19)
                drawBox(canvas, data, row, col, finboxColor)
            # draw man
            if (row, col) in data.man or data.board[row][col] == 6:
                drawMan(canvas, data, row, col)
    canvas.create_rectangle(data.width/3, data.height-50, 2 * data.width/3, data.height, outline = "red")
    canvas.create_text(data.width/2, data.height-25, text = "Restart", font = "red 24 bold")

def drawWall(canvas, data, row, col):
    size = data.cellSize
    brown = rgbString(159,149,93)
    # draw wall
    canvas.create_rectangle(col * size, row * size,
                            col * size + data.cellSize,
                            row * size + data.cellSize,
                            fill=brown,
                            outline=brown)
    # draw texture lines on the wall
    for i in range(4):
        canvas.create_line(col * size, row*size + i * size/4,
                           col * size + data.cellSize,
                           row*size + i * size / 4)
    for rows in range(4):
        canvas.create_line(col*size + (rows % 2) * size/4,
                           row*size+rows*size/4,
                           col*size + (rows % 2) * size / 4,
                           row*size+ rows * size / 4+size/4)
        canvas.create_line(col * size + (rows % 2) * size / 4 + size/2,
                           row * size + rows * size / 4,
                           col * size + (rows % 2) * size / 4 + size/2,
                           row * size + rows * size / 4 + size / 4)

def drawBox(canvas, data, row, col,color): # draw boxes on desired coordinate
    size = data.cellSize
    canvas.create_rectangle(col*size,
                            row*size,
                            col*size+size,
                            row*size+size,
                            fill=color)
    shrink = size/5
    canvas.create_rectangle(col*size+shrink,
                            row*size+shrink,
                            col*size+size-shrink,
                            row*size+size-shrink,
                            fill=color)

def drawMan(canvas, data, row, col):
    # draw man on desired coordinate
    size = data.cellSize
    rx = col*size
    ry = row*size
    # draw head
    canvas.create_oval(rx+(size/3),ry+0,rx+2*size/3,ry+(size/3), fill ="black")
    # draw body
    canvas.create_line(rx+(size/2),ry+(size/3), rx+(size/2),
                       ry+(size/3) + size/3, width = 4)
    dir1=[(-1,-1), (1,-1)]
    # draw legs
    for a,b in dir1:
        canvas.create_line(rx+(size/2),
                           ry+(size/3) + 2*size/9,
                           rx + (size / 2) + a*size/4,
                           ry + (size / 3) + 2*size / 9 +b*size/4,
                           width=4)
    # draw arms
    dir2 = [(-1,1), (1,1)]
    for a,b in dir2:
        canvas.create_line(rx+(size/2),
                           ry+(size/3) + size/3,
                           rx + (size / 2) + a*size/4,
                           ry + (size / 3) + size / 3 +b*size/4,
                           width=4)

def isfinishedSokoban(data): # check if the board is completed
    for row in range(data.dimensionR):
        for col in range(data.dimensionC):  # finished when no there is no unfinished box
            if data.board[row][col] == 2:
                return False
    return True

def redrawAllSokoban(canvas, data):
    updataAll(data)
    drawAll(canvas,data)
    if isfinishedSokoban(data):  # escape when finished
        data.finished = True
        # draw some nice messages to congrats the user
        canvas.create_rectangle(0, 2*data.height/5, data.width, 3*data.height/5, fill="green")
        canvas.create_text(data.width/2, data.height/2,
                           text="You Won!",
                           fill="yellow",
                           font="blue 35 bold underline")

def runSokoban(width=700, height=850):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAllSokoban(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressedSokoban(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressedSokoban(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    initSokoban(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAllSokoban(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

def testSokobanAnimation():
    print("Running Sokoban Animation...", end="")
    #runSokoban(700, 850)   # uncomment for map 1
    #runSokoban(1000, 600)  # uncomment for map 2
    runSokoban(1000,780)  # map 3
    print("Done!")

testSokobanAnimation()

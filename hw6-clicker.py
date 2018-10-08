# Updated Animation Starter Code

from tkinter import *
from image_util import *


####################################
# customize these functions
####################################


def init(data):
    data.scrollX = data.width / 4
    data.scrollY = data.height / 4
    data.image = PhotoImage(file="hw6-image.gif", width=100, height=100)
    data.time = 0
    data.timer = 20  # 20 seconds
    data.target = []
    data.imageSize = 30  # images is 30 by 30
    data.mode = "startScreen"  # starting mode
    data.score = 0
    data.timeBonus = 0
    # set starting point for bouncing icon
    data.startingX, data.startingY = randomStartingPos(data)
    data.speedX, data.speedY = 1, 1


def mousePressed(event, data):
    if (data.mode == "playGame"):
        playGameMousePressed(event, data)


def keyPressed(event, data):
    # enter different key-press function base on mode
    if (data.mode == "startScreen"):
        startScreenKeyPressed(event, data)
    elif (data.mode == "playGame"):
        playGameKeyPressed(event, data)
    elif (data.mode == "gameOver"):
        gameOverKeyPressed(event, data)


def timerFired(data):
    # enter different timer fire base on mode
    if (data.mode == "startScreen"):
        startScreenTimerFired(data)
    elif (data.mode == "playGame"):
        playGameTimerFired(data)
    elif (data.mode == "gameOver"):
        gameOverTimerFired(data)


def redrawAll(canvas, data):
    # enter different reDrawAll base on mode
    if (data.mode == "startScreen"):
        startScreenRedrawAll(canvas, data)
    elif (data.mode == "playGame"):
        playGameRedrawAll(canvas, data)
    elif (data.mode == "gameOver"):
        gameOverRedrawAll(canvas, data)


####################################
# start screen mode
####################################

def startScreenKeyPressed(event, data):
    # enter play-game mode when pressing 'p'
    if event.char == "p":
        data.mode = "playGame"


def startScreenTimerFired(data):
    pass


def startScreenRedrawAll(canvas, data):
    # draw all elements on starting screen
    drawIcon(canvas, data)
    drawGameName(canvas, data)
    drawInstruction(canvas, data)


def drawGameName(canvas, data):
    canvas.create_text(data.width / 2, data.height / 3,
                       text="The Clicker Game",
                       font="Chalkduster 28 bold")


def drawInstruction(canvas, data):
    canvas.create_text(data.width / 2, 4 * data.height / 5,
                       text="Press \'p\' to play",
                       font="Chalkduster 18 bold", )


def drawIcon(canvas, data):
    x, y = data.startingX, data.startingY
    dx, dy = data.speedX, data.speedY
    # flip the moving direction when bounce into a wall
    if not 0 <= x + dx < data.width - data.imageSize:
        data.speedX = -dx
    if not 0 <= y + dy <= data.width - data.imageSize:
        data.speedY = -dy
    data.startingX += dx
    data.startingY += dy
    canvas.create_image(data.startingX, data.startingY,
                        anchor="nw",
                        image=data.image)


def randomStartingPos(data):
    import random
    # generate a random starting point for the bouncing icon
    randomX = random.randint(0, data.width - data.imageSize)
    randomY = random.randint(0, data.height - data.imageSize)
    return randomX, randomY


####################################
# play game mode
####################################

def playGameMousePressed(event, data):
    # check every target for potential elimination
    for target in range(len(data.target) - 1, -1, -1):
        tx = data.target[target][0]
        ty = data.target[target][1]
        s = data.imageSize
        # check if user clicked on the target
        if tx + s > event.x + data.scrollX > tx and \
                ty + s > event.y + data.scrollY > ty:
            data.target.pop(target)
            data.score += 1
            data.timeBonus += 1
            # every 5 score gives one second bonus time
            if data.timeBonus == 5:
                data.timeBonus = 0
                data.timer += 1
            return


def playGameKeyPressed(event, data):
    # every arrow click with moves the screen by data.width/10
    stepMoveX = data.width / 10
    stepMoveY = data.height / 10
    if event.keysym == "Up":
        data.scrollY -= stepMoveY
    elif event.keysym == "Down":
        data.scrollY += stepMoveY
    elif event.keysym == "Right":
        data.scrollX += stepMoveX
    elif event.keysym == "Left":
        data.scrollX -= stepMoveX


def playGameTimerFired(data):
    data.time += 1
    if data.time % 60 == 0:  # 60 is an adjustment for time.
        data.timer -= 1
        # check if time is up
        if data.timer < 0:
            data.mode = "gameOver"


def playGameRedrawAll(canvas, data):
    # draw elements on the game over screen
    canvasDraw(canvas, data)
    targerDraw(canvas, data)
    timeLeftDraw(canvas, data)
    scoreDraw(canvas, data)


def canvasDraw(canvas, data):
    canvas.create_rectangle(-data.scrollX, -data.scrollY,
                            -data.scrollX + 2 * data.width,
                            -data.scrollY + 2 * data.height,
                            width=4)


def targerDraw(canvas, data):
    targetGenerator(data)
    for target in data.target:
        x, y = target
        canvas.create_image(-data.scrollX + x, -data.scrollY + y,
                            anchor=NW, image=data.image)


def timeLeftDraw(canvas, data):
    canvas.create_text(20, 20, anchor=NW,
                       text="Time Left: %d" % data.timer,
                       font="30")


def scoreDraw(canvas, data):
    canvas.create_text(20, data.height - 20, anchor="sw",
                       text="Score:%d" % data.score,
                       font="30")


def targetGenerator(data):
    import random
    # create a random target every 500 ms
    # to compensate the slowness speed of the program
    # i adjust it to every 300 ms (which is about 500 ms in reality)
    halfSec = 30
    if data.time % (halfSec) == 0:
        # since the boarder width is 4
        # minus 2 so that targets doesn't spawn on a line
        randomX = random.randint(2, 2 * data.width - data.imageSize - 2)
        randomY = random.randint(2, 2 * data.height - data.imageSize - 2)
        data.target.append([randomX, randomY])


####################################
# game over mode
####################################

def gameOverKeyPressed(event, data):
    if event.char == "s":
        data.mode = "startScreen"
        # reset everything
        data.startingX, data.startingY = randomStartingPos(data)
        data.score = 0
        data.time = 0
        data.timer = 20
        data.scrollX = data.width / 4
        data.scrollY = data.height / 4
        data.target = []
        data.timeBonus = 0


def gameOverTimerFired(data):
    pass


def gameOverRedrawAll(canvas, data):
    # draw back ground
    canvas.create_rectangle(0, 0, data.width,
                            data.height, fill="red")
    # draw "Game Over"
    canvas.create_text(data.width / 2, data.height / 5,
                       text="Game Over",
                       font="Chalkduster 34 bold",
                       fill="white")
    # draw Score
    canvas.create_text(data.width / 2, data.height / 2,
                       text="Final Score: %d" % data.score,
                       font="Chalkduster 18 bold",
                       fill="white")
    # draw replay instruction
    canvas.create_text(data.width / 2, 4 * data.height / 5,
                       anchor="s",
                       text="Press \'s\' to start again",
                       font="Chalkduster 18 bold",
                       fill="white")


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
    data.timerDelay = 10  # milliseconds
    root = Tk()
    root.resizable(width=False, height=False)  # prevents resizing window
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


run(300, 300)
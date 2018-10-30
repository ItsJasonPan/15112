# Updated Animation Starter Code
import math
import time
import random
from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.time = time.time()
    data.circleLst = []
    data.aim = data.width / 2
    data.aimSpeed = 15
    data.smallestR = int(min(data.height, data.width)//20)
    data.radiusIncrease = 10
    data.speed = 5
    data.holding = generateCircles(data)
    data.score = 0
    data.coolDown = 0
    data.coolDownTime = 1.5

def generateCircles(data):
    import random
    y = random.randint(int(5 * data.height/6), data.height)
    number = random.choice([2,2,2,2,2,4,4,8,16])
    if number ==2:
        size = data.smallestR + 3 * data.radiusIncrease
    elif number == 4:
        size = data.smallestR + 2 * data.radiusIncrease
    elif number == 8:
        size = data.smallestR + data.radiusIncrease
    else:
        size = data.smallestR
    x = data.aim
    return [x, y, size, number]


def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if event.keysym == "space":
        if data.coolDown <= 0:
            data.holding[1] = data.height-30
            data.circleLst.append(data.holding)
            data.holding = generateCircles(data)
            data.coolDown = data.coolDownTime
    elif event.keysym == "Left":
        if data.aim >= data.holding[2] + data.aimSpeed:
            data.aim -= data.aimSpeed
    elif event.keysym == "Right":
        if data.aim <= data.width - (data.holding[2] + data.aimSpeed):
            data.aim += data.aimSpeed


def timerFired(data):
    import copy
    if data.coolDown > 0:
        data.coolDown -= 0.02
    for circle in data.circleLst[::-1]:
        x, y, r, number = circle
        newL = copy.copy(data.circleLst)
        newL.remove([x, y, r, number])
        touch, otherCircle = touched(newL, circle)
        #print(touch, otherCircle)
        #flag = False
        if touch:
            for otherCir in otherCircle:
                if otherCir[3] == circle[3]:
                    otherCir[3] *= 2
                    data.score += otherCir[3]
                    data.circleLst.remove(circle)
                    if otherCir[2] > data.smallestR:
                        otherCir[2] -= data.radiusIncrease
                    #flag =True
                    break
        #if flag: break
        if touchDouble(circle, newL):
            continue
        elif y-r > 0 and not touch:
            circle[1] -= data.speed
        elif x-r < 0 or x+r > data.width or y-r < 0: continue
        elif touch and x <= otherCircle[0][0]:
            moveClockWise(circle, otherCircle[0])
        elif touch and x > otherCircle[0][0]:
            moveCounterClockWise(circle, otherCircle[0])
        elif touch and x == otherCircle[0][0]:
            direction = random.choice(["CW, CCW"])
            if direction=="CW":
                moveClockWise(circle, otherCircle[0])
            else:
                moveCounterClockWise(circle, otherCircle[0])


def touchDouble(myCircle, newL):
    countLeftDown, countRightDown = 0, 0
    countLeftUp, countRightUp = 0, 0
    myx, myy, myr, mynumber = myCircle
    for circles in newL:
        x, y, r, number = circles
        if ((x - myx) ** 2 + (y - myy) ** 2) ** 0.5 <= myr + r+1:
            if y < myy:
                if x <= myx:
                    countLeftDown += 1
                elif x > myx:
                    countRightDown += 1
            elif y <= myy+(r**0.5):
                if x < myx:
                    countLeftUp += 1
                elif x > myx:
                    countRightUp += 1
        if countLeftDown >= 1 and countRightDown >= 1: return True
        elif countRightUp>= 1 and countLeftDown >= 1: return True
        elif countLeftUp>=1 and countRightDown >=1: return True
    return False

def touched(newL, myCircle):
    myx, myy, myr, mynumber = myCircle
    touchedLst = []
    for circle in newL:
        x, y, r, number = circle
        if ((x-myx)**2+(y-myy)**2)**0.5 <= myr + r+1 and y < myy:
            touchedLst.append(circle)
    if len(touchedLst) > 0:
        return True, sorted(touchedLst, key=lambda l: l[1])
    else:
        return False, None


def moveCounterClockWise(circle, othercircle):
    oX,oY,oR,oNumber = othercircle
    angle = (3 * math.pi/2) + math.atan((circle[0]-oX)/(circle[1]-oY))
    angle += math.pi / 120
    circle[0] = oX + math.cos(angle)*(circle[2]+oR)
    circle[1] = oY - math.sin(angle)*(circle[2]+oR)

def moveClockWise(circle, othercircle):
    oX,oY,oR,oNumber = othercircle
    angle = (3 * math.pi/2) - math.atan((oX-circle[0])/(circle[1]-oY))
    angle -= math.pi / 120
    circle[0] = oX + math.cos(angle)*(circle[2]+oR)
    circle[1] = oY - math.sin(angle)*(circle[2]+oR)

def drawCircles(canvas, data):
    for circle in data.circleLst:
        x, y, r, number = circle
        if number == 2:
            color = "linen"
        elif number == 4:
            color = "yellow"
        elif number == 8:
            color = "orange"
        else:
            color = "red"
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=color)
        canvas.create_text(x, y, text=str(number))

def drawHolding(canvas,data):
    x,y,r,number = data.holding
    y = data.height-30
    if data.aim + r > data.width:
        x = data.width-r
    elif data.aim - r < 0:
        x = r
    else:
        x = data.aim
    data.holding[0] = x
    if number == 2:
        color = "linen"
    elif number == 4:
        color = "yellow"
    elif number == 8:
        color = "orange"
    else:
        color = "red"
    canvas.create_oval(x-r, y-r,x+r,y+r,fill=color,outline=color)
    canvas.create_text(x, y, text=str(number))

def drawTimeAndScore(canvas, data):
    mytext = "Time:"+str(round(time.time()-data.time, 1))+"   Score:"+ str(data.score)
    canvas.create_text(15, data.height-15, text=mytext, anchor="w")
    if data.coolDown > 0:
        color = "red"
    else:
        color = "gray77"
    canvas.create_text(data.width/2, data.height/2,
                       text="Cool Down: "+str(abs(round(data.coolDown,1))),
                       fill= color,
                       font="Times 28 bold italic")
    canvas.create_text(data.height-15, data.height-30,
                       text="Press \"space\" to shoot",
                       fill="grey",
                       anchor="e")
    canvas.create_text(data.height-15, data.height-15,
                       text="Press \"<-\" or \"->\" to move",
                       fill="grey",
                       anchor="e")

def redrawAll(canvas, data):
    drawCircles(canvas, data)
    drawHolding(canvas, data)
    drawTimeAndScore(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='light sky blue', width=0)
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
    data.timerDelay = 0  # milliseconds
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

run(800, 800)

"""
Exception in Tkinter callback. This error occurs when you run a program using 
the Canvas library (used from Unit 2 onwards) more than once. This is a known
problem with Canvas, and is not caused by your programming. The only solution 
is to close all Python windows then re-run IDLE after each time you run your program.
"""

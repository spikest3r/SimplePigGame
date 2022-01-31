from tkinter import *
from random import randint
from config import *
from OverlapChecker import *
import os

window = Tk()
canvas = Canvas(window,width=400,height=400)
canvas.pack()
canvas.configure(bg="green")

window.title("Simple pig game | Level 1")
score = -1
toScore = 20
level = 1
win = False

class Mushroom():
    x = 0
    y = 0
    width = 18
    height = 26
    image = 0
    def __init__(self,x,y):
        self.image = PhotoImage(file=os.getcwd()+"\\mush.png")
        self.x = x
        self.y = y
    def draw(self,c):
        c.create_image(self.x,self.y,image=self.image)

class Tree():
    x = 0
    y = 0
    width = 43
    height = 42
    image = 0
    def __init__(self,x,y):
        self.image = PhotoImage(file=os.getcwd()+"\\tree.png")
        self.x = x
        self.y = y
    def draw(self,c):
        c.create_image(self.x,self.y,image=self.image)

class Tree2():
    x = 0
    y = 0
    width = 43
    height = 42
    image = 0
    def __init__(self,x,y):
        self.image = PhotoImage(file=os.getcwd()+"\\tree2.png")
        self.x = x
        self.y = y
    def draw(self,c):
        c.create_image(self.x,self.y,image=self.image)

class CubeSnake():
    x = 0
    y = 0
    width = 30
    height = 30
    image = 0
    def __init__(self):
        self.image = PhotoImage(file=os.getcwd()+"\\pig.png")
    def draw(self,c):
        c.create_image(self.x,self.y,image=self.image)
class SnakeFood():
    x = 0
    y = 0
    width = 15
    height = 15
    image = 0
    def __init__(self):
        self.image = PhotoImage(file=os.getcwd()+"\\apple.png")
    def draw(self,c):
        c.create_image(self.x,self.y,image=self.image)
    def reGen(self,c):
        if(score == 0):
            s.x = 20
            s.y = 60
        self.x = randint(0+self.width+50,400-self.height-50)
        self.y = randint(0+self.width+50,400-self.height-50)
        self.draw(c)

class Wolf():
    x = 0
    y = 0
    width = 75
    height = 56
    direction = 0 # 0 - right | 1 - left
    image = 0
    imageR = 0
    window = 0
    func = 0
    def move(self):
        if(self.direction == 0):
            if(self.x != 360):
                self.x += wolfSpeed
            else:
                self.direction = 1
        elif(self.direction == 1):
            if(self.x != 60):
                self.x -= wolfSpeed
            else:
                self.direction = 0
        update()
        self.window.after(5,self.move)
    def __init__(self,x,y,w):
        self.image = PhotoImage(file=os.getcwd()+"\\wolf.png")
        self.imageR = PhotoImage(file=os.getcwd()+"\\wolfR.png")
        self.x = x
        self.y = y
        self.window = w
    def draw(self,c):
        if self.direction == 0:
            c.create_image(self.x,self.y,image=self.imageR)
        else:
            c.create_image(self.x,self.y,image=self.image)

s = CubeSnake()
a = SnakeFood()

# Mushrooms
m1 = Mushroom(randint(60,400-18),randint(100,400-26))
m2 = Mushroom(randint(60,400-18),randint(100,400-26))
m3 = Mushroom(randint(60,400-18),randint(100,400-26))
m4 = Mushroom(randint(60,400-18),randint(100,400-26))
m5 = Mushroom(randint(60,400-18),randint(100,400-26))

# Trees
t1 = Tree(randint(60,400-18),randint(100,400-26))
t2 = Tree(randint(60,400-18),randint(100,400-26))
t3 = Tree(randint(60,400-18),randint(100,400-26))
t4 = Tree(randint(60,400-18),randint(100,400-26))
t5 = Tree(randint(60,400-18),randint(100,400-26))

# 2Trees
t21 = Tree2(randint(60,400-18),randint(100,400-26))
t22 = Tree2(randint(60,400-18),randint(100,400-26))
t23 = Tree2(randint(60,400-18),randint(100,400-26))
t24 = Tree2(randint(60,400-18),randint(100,400-26))
t25 = Tree2(randint(60,400-18),randint(100,400-26))

# Wolfs
# X RANGE 60-360
w1 = Wolf(60,120,window)
w2 = Wolf(360,280,window)
w2.direction = 1

def update():
    if win == False:
        canvas.delete("all")
        canvas.create_text(95,20,text="Score: " + str(score) + " | You need: " + str(toScore),fill="yellow",font=('Arial',12))
        if level == 1:
            m1.draw(canvas)
            m2.draw(canvas)
            m3.draw(canvas)
            m4.draw(canvas)
            m5.draw(canvas)
        if level == 2:
            w1.draw(canvas)
            w2.draw(canvas)
        a.draw(canvas)
        s.draw(canvas)
        t1.draw(canvas)
        t2.draw(canvas)
        t3.draw(canvas)
        t4.draw(canvas)
        t5.draw(canvas)
        t21.draw(canvas)
        t22.draw(canvas)
        t23.draw(canvas)
        t24.draw(canvas)
        t25.draw(canvas)
    else:
        canvas.delete("all")
        canvas.create_text(190,200,text="You win!",font=("Lucida Console",40))

def forward(event):
    if(s.y != 18):
        s.y = s.y - cubeSpeed
        checkCollision()
        update()

def backward(event):
    if(s.y != 384):
        s.y = s.y + cubeSpeed
        checkCollision()
        update()

def left(event):
    if(s.x != 20):
        s.x = s.x - cubeSpeed
        checkCollision()
        update()

def right(event):
    if(s.x != 383):
        s.x = s.x + cubeSpeed
        checkCollision()
        update()

window.bind_all('<KeyPress-Left>',left)
window.bind_all('<KeyPress-Right>',right)
window.bind_all('<KeyPress-Up>',forward)
window.bind_all('<KeyPress-Down>',backward)

def checkMushrooms():
    cm1 = OverlapChecker.isRectangleOverlap([s.x,s.y,s.x+30,s.y+30],[m1.x,m1.y,m1.x+m1.width,m1.y+m1.height])
    cm2 = OverlapChecker.isRectangleOverlap([s.x,s.y,s.x+30,s.y+30],[m2.x,m2.y,m2.x+m2.width,m2.y+m2.height])
    cm3 = OverlapChecker.isRectangleOverlap([s.x,s.y,s.x+30,s.y+30],[m3.x,m3.y,m3.x+m3.width,m3.y+m3.height])
    cm4 = OverlapChecker.isRectangleOverlap([s.x,s.y,s.x+30,s.y+30],[m4.x,m4.y,m4.x+m4.width,m4.y+m4.height])
    cm5 = OverlapChecker.isRectangleOverlap([s.x,s.y,s.x+30,s.y+30],[m5.x,m5.y,m5.x+m5.width,m5.y+m5.height])
    cms = {cm1,cm2,cm3,cm4,cm5}
    returner = False
    for cm in cms:
        if(cm == True):
            returner = True
            break
    return returner

def checkWolfs():
    cw1 = OverlapChecker.isRectangleOverlap([s.x,s.y,s.x+30,s.y+30],[w1.x,w1.y,w1.x+w1.width,w1.y+w1.height])
    cw2 = OverlapChecker.isRectangleOverlap([s.x,s.y,s.x+30,s.y+30],[w2.x,w2.y,w2.x+w2.width,w2.y+w2.height])
    cws = {cw1,cw2}
    returner = False
    for cw in cws:
        if(cw == True):
            returner = True
            break
    return returner

def checkCollision():
    check = OverlapChecker.isRectangleOverlap([s.x,s.y,s.x+30,s.y+30],[a.x,a.y,a.x+15,a.y+15])
    mCheck = checkMushrooms()
    wCheck = checkWolfs()
    if check == True:
        global score
        global toScore
        global level
        global win
        score = score + 1
        a.reGen(canvas)
        canvas.create_rectangle(0,0,400,400,fill="black")
        update()
        if score >= toScore:
            if(level == 1):
                level = 2
                toScore = 30
                score = 0
                window.after(5,w1.move)
                w2.direction = 1
                window.after(5,w2.move)
                window.title("Simple pig game | Level 2")
            elif(level == 2):
                win = True
                window.title("Simple pig game | You win!")
                update()
    if (mCheck == True and level == 1) or (wCheck == True and level == 2):
        score = 0
        a.reGen(canvas)

checkCollision()
mainloop()
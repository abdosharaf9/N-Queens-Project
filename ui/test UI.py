from turtle import *

#Main Screen
win = Screen()
win.title("N-Queen Problem")
win.bgcolor("#dfe6dc")
win.setup(500,550)
win.tracer(0)
win.setworldcoordinates(0,0,500,550)

#Draw Board Cell
def cell(n,x,y,fill_color):
    celltu=Turtle()
    celltu.hideturtle()
    celltu.up()
    celltu.goto(x,y)
    celltu.down()
    celltu.begin_fill()
    celltu.fillcolor(fill_color)
    for i in range (4):
        celltu.fd(400/n)
        celltu.rt(90)
    celltu.end_fill()

#Draw Board
def board(n):
    x=50
    y=450
    for i in range (n):
        for j in range (n):
            if (i+j)%2==0:
                cell(n,x,y,"#baca44")
            else:
              cell(n,x,y,"#eeeed2")
            x+=400/n
        x=50
        y-=400/n 

#Queens
def queen(c,r,n):
    q=Turtle()
    q.hideturtle()
    q.up()
    posX = 50 + (r * 400 / n) - (0.5 * 400 / n)
    posY = 50 + (c-1) * (400 / n)
    q.goto(posX,posY)
    q.color("#1f1f1f")
    q.write("♛",align="center",font=("Arial",int((400/n)*0.6),"bold"))

#Input Screen
def sc1():
    #Input N Of Queens
    tu=Turtle()
    tu.up()
    tu.hideturtle()
    tu.goto(250,350)
    tu.color("#1f1f1f")
    tu.write("N-Queens:",align="center",font=("Arial","32","bold"))
    n=win.numinput("N-Queen Problem", "Number Of Queens:", 1, minval=1, maxval=100)
    # TODO: Execute the algo
    sc2(int(n), [4, 3, 8, 5, 7, 1, 3, 6], 100, 28)

#Excution Screen
def sc2(n, chromosome, gens, fit):
    #Number Of Attempts
    tu=Turtle()
    tu.up()
    tu.hideturtle()
    tu.goto(250,475)
    tu.color("#1f1f1f")
    # TODO: If you can change the color
    tu.write(f"Attempts: {gens} - Last fittest: {fit}",align="center",font=("Arial","22","bold"))
    board(n)
    for i in range(len(chromosome)):
        queen(i+1,chromosome[i],n)


sc1()
update()
done()
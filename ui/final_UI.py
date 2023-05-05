from turtle import *

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
    x=100
    y=450
    for i in range (n):
        for j in range (n):
            if (i+j)%2==0:
                cell(n,x,y,"#baca44")
            else:
              cell(n,x,y,"#eeeed2")
            x+=400/n
        x=100
        y-=400/n 

#Queens
def queen(col,row,n):
    q=Turtle()
    q.hideturtle()
    q.up()
    posX = 100 + (row * 400 / n) - (0.5 * 400 / n)
    posY = 50 + (col-1) * (400 / n)
    q.goto(posX,posY)
    q.color("#1f1f1f")
    q.write("♛",align="center",font=("Arial",int((400/n)*0.6),"bold"))

#Input Screen
def sc1(win):
    #Input N Of Queens
    tu=Turtle()
    tu.up()
    tu.hideturtle()
    tu.goto(300,375)
    tu.color("#1f1f1f")
    tu.write("N-Queens:",align="center",font=("Arial","32","bold"))
    n=win.numinput("N-Queen Problem", "Number Of Queens (Integer):", 1, minval=1, maxval=100)
    tu.clear()
    return int(n)


#Excution Screen
def sc2(n,chromosome):
    #Number Of Attempts
    tu=Turtle()
    tu.up()
    tu.hideturtle()
    tu.color("#1f1f1f")
    board(n)
    for i in range(len(chromosome)):
        queen(i+1,chromosome[i],n)

#Excution Screen Text If Solution Found
def sc2_solution(gens):
    #Number Of Attempts
    tu=Turtle()
    tu.up()
    tu.hideturtle()
    tu.goto(300,525)
    tu.color("#00a613")
    tu.write("Solution Found!",align="center",font=("Arial","30","bold"))
    tu.goto(300,475)
    tu.color("#1f1f1f")
    tu.write(f"Found In Generation: {gens}",align="center",font=("Arial","22","bold"))

#Excution Screen Text If Limit Reached
def sc2_limit(gens,fit):
    #Number Of Attempts
    tu=Turtle()
    tu.up()
    tu.hideturtle()
    tu.goto(300,525)
    tu.color("#fa2d00")
    tu.write("Limit Reached!",align="center",font=("Arial","30","bold"))
    tu.goto(300,475)
    tu.color("#1f1f1f")
    tu.write(f"Fittest: {fit}   -   Attempts: {gens}",align="center",font=("Arial","22","bold"))


def no_solution(n):
    tu=Turtle()
    tu.up()
    tu.hideturtle()
    tu.goto(300,350)
    tu.color("#fa2d00")
    tu.write("Sorry!",align="center",font=("Arial","42","bold"))
    tu.goto(300,275)
    tu.color("#1f1f1f")
    tu.write("The Problem Can't Be Solved",align="center",font=("Arial","26","bold"))
    tu.goto(300,225)
    tu.write(f"When N = {n}",align="center",font=("Arial","26","bold"))


# sc1()
# sc2_solution(100)
# sc2_limit(100,28)
# update()
# done()
tt.tracer(1)
s.bgcolor("black")
def sq(x,y,f):
    t=tt.Turtle()
    t.shape("square")
    t.speed(0)
    t.shapesize(2)
    t.penup()
    t.goto(x,y)
    if f:
        t.color("blue")
    else:
        t.color("white")
x=-300
f=True
for i in range(1,9):
    y=300
    for j in range(1,9):
        sq(x,y,f)
        y-=40
        f=not f
    x+=40
    f=not f
tt.update()
tt.done()
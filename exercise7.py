import turtle as t 
t.shape("turtle")
t.speed(10)
side = 50
angle = 90
for i in range(0,4):
    t.forward(side)
    t.left(angle)
t.up()
t.goto(0,side)
t.down()
for i in range(0,4):
    t.forward(side)
    t.left(angle)
t.up()
t.goto(side,0)
t.down()
for i in range(0,4):
    t.forward(side)

    t.left(angle)
t.up()

t.goto(side,side)
t.down()
for i in range(0,4):
    t.forward(side)
    t.left(angle)
for i in range(0,3):
    t.left(angle)
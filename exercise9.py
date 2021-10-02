import turtle as t
t.shape("turtle")
t.speed(5)
a = 170
for i in range(0,3):
    t.circle(100)
    t.up()
    t.forward(a)
    t.down()
t.up()
t.goto(90,-150)
t.down()
t.circle(100)
t.up()
t.forward(a)
t.down()
t.circle(100)
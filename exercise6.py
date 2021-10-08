import turtle as t 
t.shape("turtle")
x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))

t.goto(x1,y1)
t.goto(x2,y2)

d = (x1 -x2)**2 +(y1 -y2)**2
t.write(str(d**0.5))






import turtle as t
t.shape("turtle")

s = t.textinput("","도형을 입력하세요 : ")
if s =="사각형":
    s = t.textinput("","가로 : ")
    w = int(s)
    s = t.textinput("","세로 : ")
    h =int(s)
    for i in range(0,4):
        t.fd(w)
        t.left(90)
        t.fd(h)
elif s =="삼각형":
    s = t.textinput(""," 한 변: ")
    y = int(s)
    for i in range(0,3):
        t.fd(y)
        t.left(120)
else:
    s = t.textinput("","반지름 : ")
    r = int(s)
    t.circle(r)   
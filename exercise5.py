import random as r
x1 = r.randint(1,100)
x2 = r.randint(1,100)

print(x1,"-",x2,"=",(x1-x2))
if x1>x2:
    print("맞았습니다.")
elif x1==x2:
    print("0입니다")
else:
    print("x2가 x1보다 클 수 없습니다.")
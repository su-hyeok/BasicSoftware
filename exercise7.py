import time as t 
fseconds = t.time()

m = (fseconds //60) % 60
c = (fseconds //60) // 60 % 12

print("현재시간(영국 그리니치 시각) : " + str(c)+"시"+str(m)+"분")


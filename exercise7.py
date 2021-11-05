import random as r
number = int(input("복권 번호를 입력하세요: "))
num = r.randint(1,100)
print("당첨번호는 %d입니다" %(num))
digit1 = number//10
digit2 = number%10

num1 = num//10
num2 = num%10

if num ==number:
    print("상금은 100만원입니다.")
elif digit1 == num1 or digit1 ==digit2 or digit2 == num1 or digit2 ==num2:
    print("상금은 50만원입니다.")
else:
    print("상금은 없습니다.")
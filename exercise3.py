number = int(input("정수를 입력하시오 : "))

number1 = number % 10
number2 = (number //10) % 10
number3 = (number //100) % 10
number4 = (number //1000) % 10

print("자리수 합 : " + str(number1 + number2 + number3 + number4))

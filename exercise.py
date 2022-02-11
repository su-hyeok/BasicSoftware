import random

#문제를 출제하는 함수
def make_question():
    operand1 = str(random.randint(1, 100))	
    operand2 = str(random.randint(1, 100))
    operator = random.randint(1,2)		


    if (operator == 1):
        q = operand1 + ' + ' + operand2
    if (operator == 2):
        q = operand1 + ' - ' + operand2
    return q

correct_1 = 0
wrong_1 = 0

while True:
    quit = int(input("문제를 푸시려면 00제외 입력,문제를 풀지 않고 종료하려면 00입력:"))
    if quit == 00:
        break
    question = make_question()		
    print(question)			
    user_1 = int(input("= "))	
    answer_1 = round(eval(question), 2)
    
    if (user_1 == answer_1):
        print("정답!")
        correct_1 = correct_1 + 1
    else :
        print("오답!")
        print("정답 : ",answer_1)
        wrong_1 = wrong_1 + 1

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("정답 수 :", correct_1, "오답 수 :", wrong_1)






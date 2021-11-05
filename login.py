id ='ilovepython'
pw = 1234
i = input("아이디를 입력하세요 : ")
p = int(input("패스워드를 입력하세요 : "))
if id == i:
    if pw == p:
        print("로그인성공")
        print("환영합니다")
    else:
        print("패스워드입력이 잘못되었습니다")
else:
    print("아이디 입력이 잘못되었습니다")


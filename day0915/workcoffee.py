
# 반복문, if~elif~else 권장
# 논리연산 and or

money, k, j = 0,0,9
message  = '안내'
flag = True

money = int(input('요금을 입력 하세요 ?  '))
while flag:
    print("\n*--------- 커피 자판기 --------- *")
    print("1.커피(200)  2.코코아(250)  9.종료")
    j = int(input("메뉴를 선택하세요>>> "))
    if j == 9:  
        print('초간단 주문 프로그램 종료합니다')
        print(money ,'원 잔액을 반환합니다 ')
        flag = False
    elif ((j == 1 and money < 200) or (j == 2 and money< 250)):
        print("주문음료 요금이 부족합니다")
    elif j == 1: 
        print("커피 주문 성공입니다 맛있게 드세요"); 
        money = money - 200
        print('현재잔액은 ', money , '원입니다')
    elif j == 2: 
        print("코코아 주문성공입니다 맛있게 드세요"); 
        money = money - 250
        print('현재잔액은 ', money , '원입니다')
    else:        
        print("번호를 잘못 입력하셨습니다")




















print()
print()

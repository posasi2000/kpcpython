import random

# 총게임횟수 5회 
# 람다식X, 정규식X, 함수구현X, 리스트X, 파일처리X

flag = True 
cnt = 0
com=random.randint(1,101)
# print("com=",com)

while  flag :
    cnt = cnt + 1
    if cnt > 5: 
        print('\n게임의 제한횟수가 5회입니다')
        print('게임프로그램을 종료합니다 ')
        print(f'컴퓨터의 발생난수 {com} 숫자 입니다')
        break
    my = input(f'{cnt}회 숫자입력(quit종료)? ') 
    # 에러my = input(cnt,'회 숫자입력(quit종료)? ') 
    if my=='quit' or my=='q' :
        print('ㄴ프로그램을 종료합니다\n')
        break
    su=int(my) #문자로 받은값을 숫자로 변환
    if(su==com):
        print('ㄴ빙고정답입니다 게임을 종료합니다\n')
        break; 
    elif(su>com):
        print(f'ㄴ{su}숫자보다 작습니다 ')
    else:
        print(f'ㄴ{su}숫자보다 큰수입니다')


print()

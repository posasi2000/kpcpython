# random난수 이용  import random필요
import random

com=random.randint(1,45)
print("com=",com)
result = True 

while  result :
    my = input("\n숫자입력(exit/quit종료) >>> ")
    if my=='quit' or my=='q' or my =='exit':
        print('프로그램을 종료합니다')
        break
    su=int(my)
    if(su==com):
        print("빙고게임끝 ")
        break; 
    elif(su>com):
        print(su , "숫자보다 작습니다 ")
    else:
        print(su , "숫자보다 큰수입니다 ")










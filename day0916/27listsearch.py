# 리스트 항목 검색
color=['yellow','red','blue','purple','orange']

while True:
    my=input('\n원하는 칼라입력? ')
    if my in color:
        print(my +' 데이터 있네요')
        print("결과:", my in color)
    elif my=='q' or my=='quit' or my=='exit':
        print('프로그램을 종료합니다')
        break
    else:
        print( my+ ' 데이터가 없습니다')
        print("결과:", my in color)
       
print('칼라검색 프로그램을 종료합니다\n') 


data = [1, 2, 3, 4, 5]
try:
    na=int(input("찾을 숫자 입력? "))
    if na in data:  
        print(data,"찾는숫자가 존재합니다")
        print("결과:", na in data)
    else:
        print(data," 데이터에 없는  숫자입니다")
        print("결과:", na in data)
except Exception as ex:
    print(ex,'에러가 발생했습니다')


'''
message = ['spam', 'ham', 'spam', 'ham', 'spam']

dummy = []
for i in message :
    if i == 'spam' :
        tmp = 1
        dummy.append(tmp)
    elif i == 'ham' :
        tmp = 0
        dummy.append(tmp)

print(dummy)  # [1, 0, 1, 0, 1]
print( [1 if k=='spam' else 0 for k in message]) #[1, 0, 1, 0, 1]
print()


print( [i for i in message if 'spam' in i] )  #문자조건
print( [i for i in message if i == 'spam' ] ) #문자조건
'''
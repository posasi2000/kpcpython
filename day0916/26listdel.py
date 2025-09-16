# 리스트 항목 삭제
'''
# pop() : 맨 뒤 요소부터 제거
# pop(위치) : 특정 위치의 요소 제거
# remove(값) : 삭제 대상 값 지정
# del 리스트명[인덱스] : 특정 위치의 요소 제거
# clear() 완전삭제
# [시작:끝-1] = [ ] 구간별삭제
'''


dt = [7,  9, 'kim', 10, 'F',  15]
dt.pop() #맨끝껏 15삭제 
print(dt) #[7, 9, 'kim', 10, 'F']

dt = [7,  9, 'kim', 10, 'F',  15]
dt.pop(2) #2번째 kim삭제
print(dt) #[7, 9, 10, 'F', 15]
print()

dt = [7,  9, 'kim', 10, 'F',  15]
# 에러 dt.remove(33) 33데이터값이 없어서 에러 
dt.remove(9) #데이터값 9삭제 
print(dt)  #[7, 'kim', 10, 'F', 15]

dt = [7,  9, 'kim', 10, 'F',  15]
del dt[2:] #2번째부터 끝까지 삭제 
print(dt)  #[7, 9]
print()

dt = [7,  9, 'kim', 10, 'F',  15]
dt.clear()  #완전삭제=전체삭제
print(dt)   #결과 [ ]

dt = [7,  9, 'kim', 10, 'F',  15]
dt[2:5]=[]  # 2번째부터 5-1까지 삭제
print(dt)   #[7, 9, 15]

'''
dict삭제처리
print('1.등록  2.전체출력  3.수정  4.삭제  5.검색  9.종료 ')
num = input('>>> ')
elif num == '4' :
    name = input('삭제메뉴이름 입력? ')
    if menu.get(name) == None :
      print(name, '삭제항목 메뉴key 없습니다')
    else:
      menu.pop(name)
      print(name,'삭제처리 성공했습니다')
'''
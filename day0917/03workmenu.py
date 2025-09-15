'''
- 딕트 등록,전체출력,종료, 검색
- 반복문,제어
- 입력,형변환
'''

import sys

menu = {}
flag = True
num = '9'  #문자열로 받게 했습니다 

while flag:
  print()
  print('1.등록  2.전체출력  3.수정  4.삭제  5.검색  9.종료 ')
  num = input('>>> ')

  if num == '1':
    name = input('메뉴이름입력? ') 
    price = int(input('메뉴가격입력? ')) 
    menu[name] = price 
    print(f'{name}딕트등록 성공했습니다')
  elif num == '2' :
    for k in menu:
      print(k, ':' , menu[k] )
  elif num == '3' :
    name = input('수정메뉴이름 입력? ')
    if menu.get(name) == None :
      print(name, '수정항목 메뉴key 없습니다')
    else:
      price = int(input('수정 가격입력? ')) 
      menu[name] = price 
      print(name,'수정처리 성공했습니다')
  elif num == '4' :
    name = input('삭제메뉴이름 입력? ')
    if menu.get(name) == None :
      print(name, '삭제항목 메뉴key 없습니다')
    else:
      menu.pop(name)
      print(name,'삭제처리 성공했습니다')
  elif num == '5' :
    name = input('검색메뉴이름 입력? ')
    if menu.get(name) == None :
      print(name, '항목 메뉴key 없습니다')
    else:
      print(name, ':', menu[name])
  elif num == '9' :
    print('프로그램을 종료합니다\n') 
    sys.exit()
    flag = False
  else :
    print('번호를 잘못 입력 했습니다\n')

# 신규등록, 전체출력, 수정, 삭제, 한건조회 처리 
# 딕트에서 새로운항목 함수사용불가 add,append,insert 
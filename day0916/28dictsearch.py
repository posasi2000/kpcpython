# dict 

mysite  = { 1:'네이버', 2:'카카오' } #딕트 dict
print(mysite) #{1: '네이버', 2: '카카오'}

#해결1]   3:파이썬등록
mysite[3] = '파이썬'
print(mysite)

#해결2] 네이버대신 아마존
mysite[1] = '아마존'
print(mysite)
print()

#해결3]  2값 검색할때 mysite.get(2)추천
print(mysite[2])      #[키값]  없으면 실행에러 비권장
print(mysite.get(2))  #get()함수  없으면 None 

#해결4]  3,5값 있는지 체크 in 
print( 5 in mysite ) #False
print( 3 in mysite ) #True
print()

# 다시 딕트 초기화및 for반복문출력
mysite  = { 1:'네이버', 2:'카카오', 3:'파이썬'}
for k in mysite:
    print(k, ':', mysite[k])
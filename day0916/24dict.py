# dict구조  key =  value

# mysite = dict()
# mysite['naver'] = 'www.naver.org'
# mysite['kakao'] = 'www.kakao.org'
# mysite['python'] = 'www.python.com'

# 한번에 나열 json형태처럼 기술 
mysite = { 
   'kt' : 'www.kt.org' ,
   'sk' : 'www.sk.org' ,
   'bc' : 'www.bc.org' 
}

# 순서번호 출력
for i, e  in enumerate(mysite): 
  print(i,e, ':', mysite[e])

print()
for k,v in mysite.items():
  print(k, ':', v) 

print()
for k in mysite:
  print(k, ':', mysite[k])

print()
print(mysite['bc'])     # www.bc.org출력
print(mysite.get('bc')) # www.bc.org출력
print(mysite.get('ab')) # None출력
# dict구조  key =  value

mysite = dict()
mysite['naver'] = 'www.naver.org'
mysite['kakao'] = 'www.kakao.org'
mysite['python'] = 'www.python.com'

print(mysite)
print()

#문제1  'kakao검색 
print(mysite['kakao'])
print()

#문제2   add(),insert(),append() 함수사용안됨 
mysite['google'] = 'www.google.com'
print(mysite)
print()

#문제3 기존키값에 새로운값을 대입 
mysite['naver'] = 'www.java.com'
print(mysite)
print()

#문제4 카카오 다시 가져오기 get() 키값 검색시 없으면 None출력 
print(mysite.get('daum'))  # None출력 
print(mysite.get('kakao')) # 값출력

#문제5 naver키값 있는지 없는지 확인 
print('naver' in  mysite) # True 

# 항목 삭제 
mysite.pop('naver')
print(mysite)
# 전체삭제 mysite.clear() 
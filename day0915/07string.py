# 주석 len(문자열), 문자열.upper(), 문자열.lower(), msg.split(), msg.capitalize())

jumin = '971224'
message = '인공지능파이썬'
board = '안내게시판'
msg = 'Today is a Coffee Lg Test'

print('문자열길이 확인 =', len(msg))
# 에러 print('문자열길이 확인 =', msg.len())
print(msg)
print(msg.upper())
print(msg.lower())

msg = 'big data is python lnaguage'
print(msg.capitalize()) # 첫글자만 대문자화 
print()

print(msg.split()) # 리스트 단어로 자동 분리
msg = 'big data is python '
print(list(msg)) # 한글자씩 분리 현재는 비추천 


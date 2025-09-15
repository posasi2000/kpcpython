# 문자열추출 [시작:끝-1]
# join(), find(), index(), split(), endswith(), zfill()
# replace(변경전, 변경적용), ord(), chr(숫자)
jumin = "981231-2134569"
print("생년월일 : " + jumin[0:6]) # 981231
print("생년월일 : " + jumin[:6])  # 981231 
print("뒤 7자리 : " + jumin[7:])  # 2134569
print("뒤 7자리 : " + jumin[-7:]) # 2134569 비권장
print("뒤 7자리 : " + jumin[-1]) # 맨끝에 있는 숫자 9출력
print()

jumin = "981231-5234567"
print("년 : " + jumin[0:2]) # 0 ~ 2앞 98 나이때문에
print("월 : " + jumin[2:4]) # 2 ~ 4앞 12
print("일 : " + jumin[4:6]) # 4 ~ 6앞 31
print()


import time
time.sleep(1)
data='pythonAI is best choice'
print(data.find('best'))  # 위치 12
print(data.index('best')) # 위치 12
print(data.find('kim')) # 없으면 -1출력
# 에러print(data.index('kim')) #None예상대신 에러발생 ValueError: substring not found

a = ','
ret = a.join(data)
print(ret)
print()

my = 'python is best language'
# 변경 replace(변경전, 변경적용)
print(my)
print(my.replace('best','BigData'))
print()


msg = "python  hongildong python monday"
print(msg)
print(msg.split()) #공백기준으로 분리 list화
print()

msg2 = 'testing python pdf'
print( msg2.endswith("pdf") ) #True
print( msg2.endswith("gif") ) #False
print()

print("42".zfill(7) )  # '00042'
print("-42".zfill(7) ) # '-0042'
print()

# 8bit = 1Byte 
# 7bit 체계 ascii 
#  ord() & chr()
print(ord('A')) #65
print(ord('a')) #97
print(ord('0')) #48
print(ord('9')) #57
print()
print(chr(65))
print(chr(97))
print(chr(48))
print(chr(57))


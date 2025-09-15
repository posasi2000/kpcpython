# 주석 문자열추출[시작:끝-1]

jumin="981230-2690257"
month = jumin[2:4]
day = jumin[4:6]
print(month,'월', day,'일 생일입니다')

my = jumin[7]
if jumin[7]=='1':
   print('남자입니다')
elif my=='2' :
    print('여자입니다')  
else:
   print('성별오류')

print()
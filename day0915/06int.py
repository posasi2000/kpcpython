# 주석 int()정수화, str()문자열화

jumin = '980724' #주민번호 6자릿수 
print(jumin)
#에러 print(jumin + 6812)  #에러 TypeError: can only concatenate str (not "int") to str
print(int(jumin) + 6812) # 987536
print(type(jumin)) # <class 'str'>
print(len(jumin))  # 6자릿수
print(jumin + str(7321)) # 9807247321
print()


import datetime
dt = datetime.datetime.now()
print('현재날짜및 시간 출력 ',dt)
current_year = dt.year
jumin = "951230-1835064" 
year = int(jumin[0:2]) + 1900
print(f"현재 당신은 나이는 {current_year-year}세 입니다")
print()

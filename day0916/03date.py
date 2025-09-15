# 날짜,시간 import구문 필수

import datetime
import time

dt = datetime.datetime.now()
print(dt)
print()

print(dt.year,'년', dt.month,'월',dt.day,'일')
print(dt.hour,'시',dt.minute,'분',dt.second,'초')
print()

print(dt.strftime('현재날짜 %Y년-%m월-%d일'))
print(dt.strftime('현재시간 %H시-%M분-%S초'))
print()

time.sleep(1) #1초 지연
current_year = dt.year
jumin = '951230-1835064'

year = int(jumin[0:2]) + 1900 
print(f'현재 당신은 나이는 {current_year-year}세 입니다')
print()
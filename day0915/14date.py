import datetime
dt = datetime.datetime.now()
# print(dt)
print(dt.year, "년", dt.month, "월", dt.day, "일")
print(dt.hour, "시", dt.minute, "분", dt.second, "초")
print()

current_year = dt.year
jumin = "951230-1835064" 
year = int(jumin[0:2]) + 1900
print(f"현재 당신은 나이는 {current_year-year}세 입니다")
print()

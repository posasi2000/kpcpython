'''
조건 if ~ else  성적처리로 이해 
if 조건 :
      조건만족시처리
else :
      조건불만족처리
'''

kor, eng, total = 90, 45, 0
avg = 0.0
result = '안내문'
grade = 'F' # 학점관리 grade변수 

total = kor + eng 
avg = float(total) / 2

if avg >= 70 :
  result = '축합격'
else :
  result = '재시험'
  
if avg >= 90 :
  grade = 'A'
elif avg >= 80 :
  grade = 'B'
elif avg >= 70 :
  grade = 'C'
elif avg >= 60 :
  grade = 'D'
else:
  grade = 'F'

print(f'점수 = {total}')
print(f'평균 = {avg}')
print(f'학점 = {grade}')
print(f'{result} 대상자 입니다')
print()
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

total = kor + eng 
avg = float(total) / 2

if avg >= 70 :
  result = '축합격'
  print(f'{result} 대상자 입니다')
else :
  result = '재시험'
  print(f'{result} 대상자 입니다')


print(f'결과점수 = {total}')
print(f'결과평균 = {avg}')
print()
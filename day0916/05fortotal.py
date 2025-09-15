# for반복문 변수  in  range(숫자)

cnt, total = 0,0

for i in range(10,21,1) :
  cnt = cnt + 1
  if cnt > 5:
    break
  total = total + cnt
  print(cnt, end='  ')

print(f'합계={total}')

'''
1  2  3  4  5  합계=15
'''


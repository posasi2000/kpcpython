# for, while 반복문 구구단 출력

dan, i = 7, 0

print('for반복문으로 구구단출력')
for k in range(1,10) : 
  print(f'{dan} * {k} = {(dan*k)}')


print()
print('while반복문으로 구구단출력')
while True:
  i = i + 1
  print(f'{dan} * {i} = {(dan*i)}')
  if i == 10:
    break


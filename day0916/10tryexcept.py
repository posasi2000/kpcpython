# try~except 예외처리

num1, num2, total, mok = 0,0,0,0

try:
  num1 = int(input('num1 입력>>> '))  # 30
  num2 = int(input('num2 입력>>> '))  # 7
  total = num1 + num2
  mok = num1 / num2 
except Exception as ex:
  print(f'에러이유:{ex}\n처리오류입니다 \n확인부탁드립니다\n')

print(f'{num1} + {num2} = {total}')
print(f'{num1} / {num2} = {mok}')
print(f'{num1} / {num2} = {round(mok,2)}')
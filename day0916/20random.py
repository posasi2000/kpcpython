# 난수 import random
# random.randint(1,45) 1~45사이 정수형 숫자 발생

import random

for k in range(6) :
  a = random.randint(1,45)
  print(f'{a}' , end=' ')


'''
최대단점은 중복숫자 발생
21 35  19 35 34 37 
19 38  39 22 10 22 
13 14  26 1  8  45 
'''


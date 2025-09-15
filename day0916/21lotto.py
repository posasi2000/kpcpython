# 난수 import random

import random

# 총6회발생 for,while사용
lotto = []
lotto.clear()
for k in range(6) :
  com = random.randint(1,45)
  lotto.append(com)
  print(f'{com}' , end=' ')

print()
lotto.sort()
for j in lotto:
  print(j ,   end=' ')


'''
단점 숫자중복발생
12 15 26 15 25 39 
12 15 15 25 26 39 
'''

print()
print()
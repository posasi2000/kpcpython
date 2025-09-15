# 난수 import random

import random

flag = True
lotto = set() # set는 중복허용안되고, 순서가 없음 
# 리스트 lotto = []  
lotto.clear()

while flag :
  com = random.randint(1,45)
  lotto.add(com)
  if len(lotto) >= 6:
    flag = False
  print(f'{com}' , end=' ')

print()
mylotto = list(lotto)
mylotto.sort()
for j in mylotto:
    print(j ,   end=' ')



print()

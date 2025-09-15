# 난수 임포트 필수 
import random

# 문제1  1~45정수 random.randint()
# 문제2  0~1실수   random.random()
# 문제3  갯수만큼 추출  random.sample()
# 문제4  셔플  random.shuffle()

for a in range(5):
    print(random.random()) #실수

print()
lotto = list(range(1,45))
print(random.sample(lotto, 6))

my_list = ['파이썬','엘쥐','LLM','ai','kpc','캐데헌']
random.shuffle(my_list)
print(my_list)

# 람다는 일시적으로 사용하고 버리는 함수
# 람다식  map() for반복문역할
# 람다식  filter() if~else조건을 리스트적용
# 람다식  reduce() 집계처리 임포트 필요 


from functools import reduce   # 임포트  

def  myhap(x, y):
  return x + y

a = [1, 2, 3, 4, 5]
print('일반식 총합계', reduce(myhap, a) ) #람다식 아님 
print('람다식 총합계', reduce(lambda x, y: x + y, a) ) #람다식


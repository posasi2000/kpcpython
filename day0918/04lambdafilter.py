# 람다는 일시적으로 사용하고 버리는 함수
# 람다식  map() for반복문역할
# 람다식  filter() if~else조건을 리스트적용

def myExpress(n):
    msg = '결과'
    if n%2 == 0 :
        msg = '짝수'
    else:
        msg = '홀수'
    return msg


def twomydata(data):
    temp = []
    for k in data:
        if k%2 == 0:
            temp.append(k)
    return temp


# print('람다식' , (lambda n: '짝수' if n%2==0 else '홀수')(12))
# print('람다식', list(map(lambda n: n*n, list(range(1,6)) )))

su = list(range(1,11))  # 1~10숫자에서 짝수만 출력 
ret = twomydata(su)
print('일반식', ret)
f = list(filter( lambda n: n%2==0 ,su))
print('람다식', ret)
print()

# reduce() 집계함수역할 
from functools import reduce   # 임포트  
print('총합계', reduce(lambda x, y: x + y, [ 1, 2, 3, 4, 5]) ) #람다식


def  myhap(x, y):
  return x + y

a = [1, 2, 3, 4, 5]
print('총합계', reduce(myhap, a) ) #람다식 아님 
# 람다는 일시적으로 사용하고 버리는 함수
# 람다식  map() for반복문역할
# 람다식  filter() if~else조건을 리스트적용

def firstmydata(data):
    total = [ ]
    for k in data:
        gob = k*k
        total.append(gob)
    return total

a = list(range(1,6)) 
ret = firstmydata(a) 
print('일반식', ret)  
c = list(map(lambda n: n*n,a))
print('람다식', c)
print( f'람다식 {list(map(lambda n:n*n,list(range(1,6))))}' )
print()

# for반복문대신 map사용하면 좋아요 
def calc(x):
    return x*x

for i in range(1, 6):
    print(calc(i), end= ' ')  # 일반함수호출

print()
print(list(map(calc, range(1,6))))  #럼다식은 아님 
print(list(map(lambda x:x*x, range(1,6))) )  #진정한 람다식

print()
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10 ]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # [5, 7, 9]
print()
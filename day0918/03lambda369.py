# 람다식 lambda키워드기술 
# 람다식은 import 없습니다
# 람다는 일시적으로 사용하고 버리는 함수
# 람다식  map() for반복문역할
# 람다식  filter() if~else조건을 리스트적용

print( list(map(lambda x: '짝' if x % 3 == 0 else x, range(1, 21))) )
print()


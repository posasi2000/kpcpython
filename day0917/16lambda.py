# 람다식 lambda키워드기술 
# 람다식은 import 없습니다
# 람다는 일시적으로 사용하고 버리는 함수

def mysu(x):
    return  5*x+2 

print('일반식', mysu(7))

myret = lambda x: 5*x+2
print('람다식', myret(7))
print('람다식',(lambda x: 5*x+2)(7))
print(f'람다식 {(lambda x:5*x+2)(7)}')


print()
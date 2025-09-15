# 람다식 lambda키워드기술 
# 람다식은 import 없습니다
# 람다는 일시적으로 사용하고 버리는 함수

def add(x,y):
    return  x+y 

print('일반식', add(4,3))

lambdaAdd = lambda x,y: x+y
print('람다식', lambdaAdd(4,3))
print('람다식',(lambda  x,y: x+y)(4,3))
print( f'람다식 {(lambda x,y: x+y)(4,3)}' )
print()

# print('람다식 매개인자 3개 받아서 곱하기처리')
# 일반식함수 매개인자3개  myMul()  myGob()
def myGobMultiple(a,b,c):
    return a*b*c

print('일반식', myGobMultiple(3,4,5))
print('람다식', (lambda a,b,c: a*b*c)(3,4,5))


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


print('일반식' , myExpress(12))
print('람다식' , (lambda n: '짝수' if n%2==0 else '홀수')(12))

#리스트 comprehension
message = ['spam', 'ham', 'spam', 'ham', 'spam']
print( [1 if k=='spam' else 0 for k in message]) #[1, 0, 1, 0, 1]
print( ['짝수' if k%2==0 else '홀수' for k in range(1,11)])
#출력 ['홀수', '짝수', '홀수', '짝수', '홀수', '짝수', '홀수', '짝수', '홀수', '짝수']   
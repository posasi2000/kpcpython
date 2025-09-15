# list comprehension 축약식

# 일반 for반복  제곱처리
for a in range(1,11,1):
    print(a*a, end=' ')
print()

for b in range(1,11,1):
    print(pow(b,2), end=' ')


print()
print()
# list comprehension이용 제곱처리
my_list = [ c*c for c in range(1,11,1) ]
print(my_list )
print([c*c for c in range(1,11,1)])


print()
message  = 'kim lee park' 
print(message.upper()) 

names = ['kim','lee', 'park']
print( [name.upper() for name in names ] )

print()
print( [ d for d in range(1,11,1)  if d%2==0 ] ) #짝수출력

message = ['spam', 'ham', 'spam', 'ham', 'spam']
print( [1 if k=='spam' else 0 for k in message]) #[1, 0, 1, 0, 1]
print( ['짝수' if k%2==0 else '홀수' for k in range(1,11)]) # ['홀수', '짝수', '홀수', '짝수', '홀수', '짝수', '홀수', '짝수', '홀수', '짝수']  
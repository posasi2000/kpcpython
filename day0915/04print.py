# 사칙연산 + -  *  /  %

a, b, gob, hap  = 0, 0, 0, 0 #변수 초기화역할

a = 9  # 값대입 
b = 3  # 값대입 
gob = a * b # 곱하기연산 
hap = a + b # 더하기연산

print('첫번째 방법')
print(a, '*', b, '=', gob)
print(a, '+', b, '=', hap)
print()

b = 4
gob = a * b
hap = a + b
print('두번째 방법')
print('%d * %d = %d' %(a, b, gob) )  # %d정수  %f실수 %s문자 
print('%d + %d = %d' %(a, b, hap) )
print()


b = 5
gob = a * b
hap = a + b
print('세번째 방법')
print('{} * {} = {}'.format(a, b, gob) )
print('{} + {} = {}'.format(a, b, hap) )
print()

b = 6
gob = a * b
hap = a + b
print('네번째 방법')
print(f'{a} * {b} = {gob}' ) # 추천 
print(f'{a} + {b} = {hap}' ) # 추천 
print()

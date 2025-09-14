# 연산 + -  *  /  %

print(29/4)     # 7.25
print(29//4)    # 7
print(19/3)     # 6.333333333333333
print(19//3)    # 6
print()

su = -5600
print(su)
print(abs(su)) # 양수값출력 절대값
print()

print(9**2) #81
print(pow(9,2)) #81
print(pow(9,3))  #729

print(5*2) #10
print(5**2) #25
print(pow(5,2)) #25   
print()

mok = 34.56471
print(mok)
print('%.2f'%(mok))
print(round(mok,2))  #추천
print()
print('%.3f'%(mok))
print(round(mok,3)) 
print()

# 관계연산 > < == != 
a = 5
b = 7
print( a > b )   # False
print( a <= b )  # True
print( a != b)   # True
print( a == b )  # False
print( (a>3) and (b>10) ) # False
print( (a>3) or  (b>10) ) # True
print()



a,b = 4, 7
caland = a & b
calor =  a | b
print(f'{a} & {b} = {caland}') #4 & 7 = 4
print(f'{a} | {b} = {calor}')  #4 | 7 = 7
# 4 0000  0100
# 7 0000  0111
# ------------------
# & 0000  0100
# | 0000  0111


# 연산 - 산술,관계,논리,대입,비트
# 0 0000  0000
# 1 0000  0001
# 2 0000  0010
# 3 0000  0011
# 4 0000  0100
# 5 0000  0101
# 6 0000  0110
# 7 0000  0111
# 8 0000  1000
# 9 0000  1001






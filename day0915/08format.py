# format()

mok = 2347.56471
print(mok)
print('%.2f'%(mok))
print(round(mok,2)) 
print()

print('{:0>15,}원'.format(mok))  # >오른쪽맞춤
print('{:*>15,}원'.format(mok))  # 은행에서 표기
print('{:,}원'.format(mok))
print()

a,b = 9, 3  
hap = a + b 
print('{} + {} = {}'.format(a, b, hap) )
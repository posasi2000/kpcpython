# while반복문 

cnt, total = 0,0

while cnt < 10 :
    cnt = cnt + 1
    if cnt == 5:
        continue
    print(cnt, end='  ')
    total = total + cnt
    if cnt == 10:
        break


print(f'합계={total}')

'''
while반복문
1 2 3 4 6 7 8 9 10  합계=50
'''
print()

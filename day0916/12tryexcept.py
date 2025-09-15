# try~except 예외처리

x, y, total, mok = 0,0,0,0
try:
    x = int(input('x 정수입력>>> ')) 
    y = int(input('y 정수입력>>> '))  
    total = x + y
    mok = x / y 
    print()
    print(f'{x} + {y} = {total}')
    print(f'{x} / {y} = {mok}')
    print(f'{x} / {y} = {round(mok,2)}')
    print('%d / %d = %.2f'%(x, y, mok))
except:
    print('데이터처리 예외가 발생했습니다')
    print('다시 실행하세요')
print()
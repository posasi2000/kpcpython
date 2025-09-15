# input('안내문') 숫자를 입력해도 무조건 문자열로 인식
# int(), float(), round(값,자릿수)

name, age, fit  = '닉네임', 10, 7.8

name = input('이름입력>>> ') # hong입력
age = input('나이입력>>> ')  # 23입력
fit = input('피트입력>>> ')  # 4.56입력
myage  = int(age) + 10
myfit = float(fit) * 2.1

# 문제해결 혜택조건 입력한 나이 + 10, 입력한 피트 * 2.1 
# 파이썬언어는 input('안내문') 입력하면 무조건 문자열로 인식
print()
print(f'입력받은 이름 = {name}')
print(f'입력받은 나이 = {myage}')
print(f'입력받은 피트 = {myfit}')
print(f'입력받은 피트 = {round(myfit,2)}')
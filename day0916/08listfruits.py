# list 중복가능,순서있음

summer_fruits = ['수박', '참외', '체리', '포도']
for fruit in summer_fruits:
  print(fruit, end='\t')


print()
numbers = [10, 20, 30, 40, 50]
print(f'합계 = {sum(numbers)}')
# type(), int(), str(), float(), round(), pow(), len(), sum()

print()
message = 'Hello is a good word'
print(message)
print(list(message))   #한단어씩 분리
print(message.split()) #단어로 끊기
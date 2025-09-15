# 정규식 import re

import re
# re.sub(), re.findall()
# re.search()&group(),  re.match()&group(),    re.compile()&findall() 

old_text = 'The color is blue'
new_text = re.sub('blue','orange',old_text)
print(old_text)
print(new_text)
print(old_text.replace('blue','orange'))  #문자열 replace(old,new)
print()


# 숫자만추출  re.findall()함수 
data = "fruits 20 apples, 78 bananas,  34 oranges"
count = re.findall('\d+', data)  #['20', '78', '34']
print(count)
print()


data = "LLM모델 is a best PyLLM모델"  
my = re.match('LLM모델', data)
#print(my) #<re.Match object; span=(0, 6), match='Python'>
if my :   
    print(my.group(), '패턴일치 OK성공')
else:    
    print('패턴의 불일치 데이터가 없습니다')
print()


phone = "phone723-9876-1234 eztsoft"
my = re.search('\d{3}-\d{4}-\d{4}', phone)
#print(my) #<re.Match object; span=(5, 18), match='723-9876-1234'>
if my:
    print(my.group())
    print('시작위치', my.start())
    print('끝위치', my.end())


print()
s = "Apple is big company and apple is very delicious Apple my Apple"
c = re.compile('apple', re.I) #['Apple', 'apple', 'Apple', 'Apple']
# print(c) 출력 re.compile('apple', re.IGNORECASE)
print(c.findall(s))

c = re.compile('apple') #['apple']
# print(c) 출력 re.compile('apple')
print(c.findall(s))

# 정규식 import re

import re
# re.sub(), re.findall()
old_text = 'The color is blue'
new_text = re.sub('blue', 'orange', old_text)
print('원본', old_text)
print('변경', new_text)
print('변경', old_text.replace('blue','orange'))  #문자열 replace(old,new)
print()


# 숫자만추출  re.findall()함수 
data = "fruits 20 apples, 78 bananas,  34 oranges"
# count = re.findall('\d', data) #['2', '0', '7', '8', '3', '4']
count = re.findall('\d+', data)  #['20', '78', '34']
print(count)
# 정규식 import re

import re
# re.sub()
old_text = 'The color is blue'
new_text = re.sub('blue', 'orange', old_text)
print('원본', old_text)
print('변경', new_text)
print('변경', old_text.replace('blue','orange'))  #문자열 replace(old,new)
print()

phone = '010-7100-1234 박이썬'
print(phone) #전부공개

modela = re.sub('-[0-9]{4}-', '-****-',  phone)
print(modela) #010-****-1234 박이썬  권장

modelb = re.sub('[0-9]{3}-[0-9]{4}-', '***-****-',  phone)
print(modelb) #***-****-1234 박이썬  완전익명
print()

msg = 'my best $#@ 오렌지 color @#&%# 345 is orange'
result3 = re.findall( '[\w]+' , msg) #result5동일  
result4 = re.findall( '[\W]+' , msg) #result6동일   
result5 = re.findall( '[a-zA-Z0-9가-힣]+' , msg)   
result6 = re.findall( '[^a-zA-Z0-9가-힣]+' , msg)       
print('result3', result3)
print('result4', result4) 
print()

print('result5', result5) 
print('result6', result6) 


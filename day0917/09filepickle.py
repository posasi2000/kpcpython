# import 피클, 암호화이진화 보안처리 
# 피클저장 dump(), 피클열기 load()
import pickle
import time

fileName = './data/mydata.pckf' 

menu = {
    'name' : 'coffee' ,
    'price' : 2300 ,
    'kind' : ['아이스', '라떼' , '카푸치노']
}

with open(fileName , 'wb') as myfile:
    pickle.dump(menu, myfile)

print(fileName,'파일 저장성공했습니다')
print()
time.sleep(2)

file = open(fileName, 'rb')
mydata = pickle.load(file)
print(mydata)
print(fileName,'파일 열기성공했습니다')

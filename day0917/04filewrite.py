#파일처리 open('경로파일명', '모드', 인코딩)

path = './data/abc.txt'
file = open(path, 'w' , encoding='utf-8')

name = input('이름입력 : ')
age = input('나이입력 : ')
file.write(name + '\n')
file.write(age  + '\n')
file.close() 
print(path , '파일저장 성공')
print()
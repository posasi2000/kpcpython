#파일처리 open('경로파일명', '모드', 인코딩)

path = './data/abc.txt'
file = open(path, 'r' , encoding='utf-8')
data = file.read()
print(data)
file.close() 

print(path , '파일읽기 테스트 ')
#파일처리 with open('경로파일명', '모드', 인코딩) as 닉네임

path = './data/emp.txt'
with open(path, 'r' , encoding='utf-8') as myfile:
    data = myfile.read() 
    print(data)

print(path , '파일읽기 테스트 ')



'''
path = './data/emp.txt'
with open(path, 'r' , encoding='utf-8') as myfile:
    while True:
        data = myfile.readline() 
        if not data:
            break
        else:
            print(data)

print(path , '파일읽기 테스트 ')

# read(): 파일의 문장을 전체 다 읽어온다. 첫째줄부터 마지막줄까지. string으로~
# readlines () : 파일의 문장을 통채로 다 읽어온다. 첫째줄부터 마지막줄까지. list로~
# readline () :파일의 문장 한줄만 읽어온다. string으로~
'''


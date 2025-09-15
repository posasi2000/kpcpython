#파일처리 with open('경로파일명', '모드', 인코딩) as 닉네임

path = './data/emp.txt'
with open(path, 'a' , encoding='utf-8') as myfile:
    name = input('이름입력 : ')
    pay = input('급여입력 : ')
    myfile.write(name + '\n')
    myfile.write(pay  + '\n')

print(path , '파일저장 테스트 ')

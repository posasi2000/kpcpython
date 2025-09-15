import os.path

fileName = './data/abcdummy.txt'
save_path = os.path.abspath(fileName)
if not os.path.exists(save_path) :
    print('No fileName ... \n파일데이터가 없습니다 ')
else:
    with open('./data/dummy.txt' , 'r' , encoding='utf-8') as myfile:
        data = myfile.read()
        print(data)

print()

# myfile.read() 전체읽기
# myfile.readline()
# myfile.readlines()
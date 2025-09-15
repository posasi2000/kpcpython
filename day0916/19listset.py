# list는 중복허용,순서있음  set는 순서없음, 중복허용x


# list[] 중복허용, 순서있음 
subject = ['수학','역사', '제주','컴퓨터','수학','수학','물리학','제주', '수학', '제주']
print(subject)
print()

#set{ } 중복안됨, 순서없음 
title = { '수학','역사', '제주','컴퓨터','수학','수학','물리학','제주', '수학', '제주'}
print(title)
print(' -' * 30)
print()

data  = [ ] # 리스트초기화
# data  = list() # list()함수  초기화
data.append('초가을')
data.append(78)
data.append(True)
data.append(2.34)
print(data)

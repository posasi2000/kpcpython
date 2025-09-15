# 

data = [
   [1, 2, 3, 4] , 
   [5, 6, 7, 8] ,
   [9,10,11,12]
]

#문제해결 for반복문 for반복문
for row in range(len(data)): #3행
    for col in range(len(data[row])): #4열
        print(data[row][col], end='\t')
    print()


#문제해결 for반복문 for반복문
# 4행 * 열데이터 비고정 리스트 
print()
mydata = [
   [1,2,3,4,5] ,       #5열
   [6,7,890] ,        #3열
   [9,10,11,12,13] ,   #5열
   [14,1500, 16, 170]  #4열
]


for row in range(len(mydata)): # range(4) 0~3
    for col in range(len(mydata[row])):
        print(mydata[row][col], end='\t')
    print()

# 이중list처리

apart = [
     [101,102,103,104,105] , [201,202,203,204,205] , 
     [301,302,303,304,305],  [401,402,403,404,405]
]
unpaid = [ 102, 204, 303, 405 ] 

#문제해결 중첩for반복안에서 if조건   
for row in apart: 
    for col in range(5):
        if row[col] in unpaid :
            print( row[col], '호 우유 배달 중지 x') 
        else:
            print( row[col], '호 우유 배달 계속 o') 
    print()

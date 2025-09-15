# 함수생성 매개인자없음, 리턴값있음

def server_connet() :
    flag = False
    return flag

def server_error():
    message = '시스템 장애입니다'
    return message

def myData():
    userid='skyblue'
    return userid

def myPrint():
    nick = myData()
    print("유저이름은", nick,'입니다')
    

msg  = server_error()
print(msg)
print(server_error())
print()

myPrint() 


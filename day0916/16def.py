# 함수리턴값, 매개인자

def myCal(name,kor,eng): 
  print(name)
  total = kor + eng  #z변수 local블럭안에서 사용되는 변수
  return total


ret = myCal('고길동', 90,85)
print('총점 =',ret)
print()
# 함수 호출시 main명시

def test():
  kor,eng,total,avg = 0,0,0,0
  message = '결과'
  kor = 40
  eng = 85
  total = kor + eng 
  avg = total / 2 
  if avg >= 70:
    message = '축합격'
  else:
    message = '재시험'
  return total, avg, message


if __name__  == '__main__' :
    x,y,z = test()
    print(f'총점 = {x}')
    print(f'평균 = {y}')
    print(f'결과 = {z}')
    print()

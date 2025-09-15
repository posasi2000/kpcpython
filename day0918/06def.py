# 함수의 매개인자 갯수를 가변으로 지정

def hap_methon(*par):
    hap = 0
    for num in par:
      hap = hap + num
    return hap

a = hap_methon(15,4)
print('a결과 =', a)

b = hap_methon(1,2,3,4,5)
print('b결과 =', b)

c = hap_methon(4,5,7)
print('c결과 =', c)
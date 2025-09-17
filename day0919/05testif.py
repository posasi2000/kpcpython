#해결1] 홀수 짝수 구하기
# a = int(input("정수 입력>>> "))
a = 19
if a%2==0: 
    print("짝수입니다")
else: 
    print("홀수입니다")
print()



#해결2] for ~ if 
for b in range(1,31,1):
    print(b , end="\t")
    if b%5==0:
        print()

print()
cnt = 0
while True:
    cnt = cnt + 1
    print(cnt , end="\t")
    if cnt%5==0:
        print()
    if cnt == 30: break










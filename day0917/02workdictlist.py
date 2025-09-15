# dict key : [value]

score_dict = { 'kim':[100,60], 'lee':[90,77], 'goo':[82,34] }

kor_total, eng_total, kor_avg,eng_avg  = 0,0,0,0

kor_list,eng_list = [], []
for name,value  in  score_dict.items():
  kor_total = kor_total + value[0]
  eng_total = eng_total + value[1]

print('국어총점 =',kor_total)
print('영어총점 =',eng_total)
print('국어평균 =',kor_total//3)
print('영어평균 =',eng_total//3)
print()

# 변수의 초기화
kor_total, eng_total, kor_avg,eng_avg  = 0,0,0,0
for name,value  in  score_dict.items():
  print(f"{name}님 총점:{sum(value)} 평균:{sum(value)/len(value)}")
  kor_total = kor_total + value[0]
  eng_total = eng_total + value[1]
  
print('국어총점 =',kor_total)
print('영어총점 =',eng_total)
print('국어평균 =',kor_total//3)
print('영어평균 =',eng_total//3)
print()

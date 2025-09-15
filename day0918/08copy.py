# 데이터복사
import copy

a = [11, 22, 33]
b = copy.deepcopy(a) 
# b = a
a[1] = 976
print(a)
print(b)
print()
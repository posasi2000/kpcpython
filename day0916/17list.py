# list는 중복데이터가능, 순서있음, 표시[ ] 

list1 = [20, 11, 40, 50, 33]
print(max(list1))
print(min(list1))
print(sum(list1))
print()

list1.sort()                  # list1의 원소를 오름차순 정렬
print(list1)
list1.sort(reverse = True)    # list1의 원소를 내림차순 정렬
print(list1)
print()

list7 = [1, 2, 3, 4]
list8 = [10, 20, 30]
list3  = list7 + list8
print(list3) # [1, 2, 3, 4, 10, 20, 30]
print()

#슬라이싱 쪼개기  [시작:끝-1]
a_list = [70, 20, 30, 40, 50, 22, 11, 80]
print(a_list[1:5]) # [20, 30, 40, 50]
print()

list1 = [20, 10, 40, 50, 30]
print(list1)
list1.append(45) # [20, 10, 40, 50, 30, 45]
print(list1)
list1.insert(3,78) # [20, 10, 40, 78, 50, 30, 45]
print(list1)
print()
# tuple( )

mytuple = ('제주', 37.75148, 126.34136, '시청', 36.73982, 127.92851 )
print(mytuple)
mytuple = mytuple + ('대전',)
mytuple = mytuple + (35.78923,)
mytuple = mytuple + (125.65491,)
print(mytuple)
print()

mylist = list(mytuple)
mylist.append('청사')
mylist.append(36.12345)
print(mylist)
print()

mytuple = tuple(mylist)
print(mytuple)
print()
'''
ModuleNotFoundError: No module named 'faker'
pip install faker
'''

#  pip install faker
from faker import Faker

my = Faker() 
for k in range(10):
    print(my.name())

print()

for k in range(10):
    print(my.ipv4_private())
    
print()

data = Faker('ko_KR') 
for k in range(10):
    print(data.name())

print()


for k in range(10):
    print(data.address())

print()

for k in range(10):
    print(data.color())

print()





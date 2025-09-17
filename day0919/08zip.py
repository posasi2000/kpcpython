# tuple이용 zip()
numbers = (1, 2, 3)
letters = ('A', 'B', 'C')
pairs = list(zip(numbers, letters))
print(pairs) #[(1, 'A'), (2, 'B'), (3, 'C')]

import time
time.sleep(1)
numbers, letters = zip(*pairs)
print(numbers) #(1, 2, 3)
print(letters) #('A', 'B', 'C')
print()


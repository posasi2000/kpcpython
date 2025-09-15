# list comprehension 축약식

message = ['spam', 'ham', 'spam', 'ham', 'spam']

dummy = []
for i in message :
    if i == 'spam' :
        tmp = 1
        dummy.append(tmp)
    elif i == 'ham' :
        tmp = 0
        dummy.append(tmp)

print(dummy)  # [1, 0, 1, 0, 1]

# print('list comprehension')
print( [1 if k=='spam' else 0 for k in message]) #[1, 0, 1, 0, 1]

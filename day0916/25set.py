#  set중복허용x, 순서없음

mywish = set() 
mywish.add('kb')
mywish.add('연아')
mywish.add('kb')
mywish.add('bc')
mywish.add('kb')
mywish.add('연아')
mywish.add('kb')     #추가  
print(mywish)
mywish.discard('kb')  #삭제
print(mywish)


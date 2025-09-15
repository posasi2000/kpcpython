# class 생성

class Emp:
    name = '' #전역변수=속성=properties=attribute=멤버변수=class변수=m
    def __init__(self, name):
        self.name=name
        print( name, '사원입니다\n')


    def insert(self):
        print('insert함수' , self.name)
        
    def printAll(self):
        print('printAll함수' , self.name)
    
    def emp_delete(self):
        print('emp_delete함수' , self.name)
        

if __name__ == "__main__":
    object = Emp('홍길동')
    object.insert()
    object.printAll()
    object.emp_delete()
  
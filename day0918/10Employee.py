# class 생성
class Employee:
    def __init__(self, emp_id, name,  pay):
        self.emp_id = emp_id       
        self.name = name          
        self.pay = pay       

    def display_info(self):
        print(f'사번:{self.emp_id} 이름:{self.name}  급여:{self.pay}')

    def update_pay(self, new_pay):
        self.pay = new_pay
        print(f'\n{self.name}님의 월급이 {self.pay}로 변경되었습니다 ')
        

# # Employee 객체생성
emp1 = Employee(1001, "김연아",  9200)
emp2 = Employee(1002, "손흥민",  7800)

emp1.display_info()
emp2.display_info()

# 월급 수정
emp1.update_pay(12000)


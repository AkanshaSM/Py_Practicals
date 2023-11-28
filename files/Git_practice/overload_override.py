# class India:
#     def capital(self):
#         print("New Delhi")
#     def capital(self,a):
#         print("New Delhi",a)
# a=India()
# a.capital(21)

class Employee:
   def func_message(self):
     print('Welcome to Employee')
class Department(Employee):
     def func_message(self):
        print('Welcome to Department')
        print('This is inherited from Employee')
emp = Employee()
emp.func_message()
print('------------')
dept = Department()
dept.func_message()
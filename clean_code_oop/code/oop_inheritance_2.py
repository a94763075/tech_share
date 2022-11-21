class Person:
  def __init__(self, first, last):
    self.firstname = first
    self.lastname = last

class Employee(Person):
  def __init__(self, first, last, employee_id, salary):
    super().__init__(first, last)
    self.employee_id = employee_id
    self.salary = salary

class Intern(Person):
  def __init__(self, first, last, intern_id, grades):
    super().__init__(first, last)
    self.intern_id = intern_id
    self.grades = grades


spongebob = Employee('海綿', '寶寶', 'K0001', 0)
squidward = Employee('章魚', '哥', 'K0002', 24000)
print(spongebob.firstname)
# 海綿
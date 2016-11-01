class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"


    def fullname(self):
        return self.first + " " + self.last

emp_1 = Employee("Harshdeep", "Mann", "126000")
emp_2 = Employee("Test", "User", "110000")


print(emp_1.fullname())

print(Employee.fullname(emp_2))

# print('{} {}'.format(emp_1.first, emp_1.last))

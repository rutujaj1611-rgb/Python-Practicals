#Single Inheritance
class Student:
    def __init__(self, name):
        self.name = name

class Attendance(Student):
    def show(self, days_present, total_days):
        percent = (days_present / total_days) * 100
        print(self.name, "Attendance:", percent, "%")


s = Attendance("ABC")
s.show(45, 50)


#Multiple Inheritance
class Company:
    def __init__(self, cname):
        self.cname = cname

    def show_company(self):
        print("Company:", self.cname)


class Department:
    def __init__(self, dname):
        self.dname = dname

    def show_department(self):
        print("Department:", self.dname)


class Employee(Company, Department):
    def __init__(self, cname, dname, ename):
        Company.__init__(self, cname)
        Department.__init__(self, dname)
        self.ename = ename

    def show_employee(self):
        print("Employee:", self.ename)


e = Employee("Infosys", "IT", "ABC")
e.show_company()
e.show_department()
e.show_employee()
class Employee_jcs:
    def work_jcs(self_jcs):
        print("Employee performs tasks")

class Programmer_jcs(Employee_jcs):
    def work_jcs(self_jcs):
        print("Programmer writes code")

class Designer_jcs(Employee_jcs):
    def work_jcs(self_jcs):
        print("Designer creates UI designs")

employees_jcs = [Programmer_jcs(), Designer_jcs()]
for emp_jcs in employees_jcs:
    emp_jcs.work_jcs()
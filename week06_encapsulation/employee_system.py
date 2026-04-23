class Employee_jcs:
    def __init__(self_jcs, name_jcs):
        self_jcs.__name = name_jcs
        self_jcs.__salary = 0

    def set_salary_jcs(self_jcs, salary_jcs):
        if salary_jcs > 0:
            self_jcs.__salary = salary_jcs

    def get_salary_jcs(self_jcs):
        return self_jcs.__salary

emp_jcs = Employee_jcs("Ana")
emp_jcs.set_salary_jcs(30000)
print("Salary:", emp_jcs.get_salary_jcs())
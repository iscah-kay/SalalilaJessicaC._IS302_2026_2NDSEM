class Employee_jcs:
    def __init__(self_jcs, name_jcs, salary_jcs):
        self_jcs.name_jcs = name_jcs
        self_jcs.salary_jcs = salary_jcs

class Manager_jcs(Employee_jcs):
    def __init__(self_jcs, name_jcs, salary_jcs, department_jcs):
        super().__init__(name_jcs, salary_jcs)
        self_jcs.department_jcs = department_jcs

    def display_manager_jcs(self_jcs):
        print("Name:", self_jcs.name_jcs)
        print("Salary:", self_jcs.salary_jcs)
        print("Department:", self_jcs.department_jcs)

manager1_jcs = Manager_jcs("John", 50000, "IT")
manager1_jcs.display_manager_jcs()
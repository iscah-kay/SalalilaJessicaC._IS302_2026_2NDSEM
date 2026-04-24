class Student_jcs:
    def __init__(self_jcs, name_jcs, student_id_jcs, gpa_jcs):
        self_jcs.__name = name_jcs
        self_jcs.__student_id = student_id_jcs
        self_jcs.__gpa = gpa_jcs

    def get_student_info_jcs(self_jcs):
        print("Name:", self_jcs.__name)
        print("Student ID:", self_jcs.__student_id)
        print("GPA:", self_jcs.__gpa)

student1_jcs = Student_jcs("Juan", "2023-001", 1.75)
student1_jcs.get_student_info_jcs()
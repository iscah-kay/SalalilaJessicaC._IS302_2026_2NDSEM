class Student_jcs:
    def __init__(self_jcs, name_jcs, student_id_jcs, course_jcs):
        self_jcs.name_jcs = name_jcs
        self_jcs.student_id_jcs = student_id_jcs
        self_jcs.course_jcs = course_jcs
    
    def display_student_jcs(self_jcs):
        print("Name:", self_jcs.name_jcs)
        print("Student ID:", self_jcs.student_id_jcs)
        print("Course:", self_jcs.course_jcs)

student1_jcs = Student_jcs("Maria", "2023-001", "BSIS")
student1_jcs.display_student_jcs()

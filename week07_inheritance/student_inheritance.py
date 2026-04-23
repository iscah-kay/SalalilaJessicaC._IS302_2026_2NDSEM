class Person_jcs:
    def __init__(self_jcs, name_jcs, age_jcs):
        self_jcs.name_jcs = name_jcs
        self_jcs.age_jcs = age_jcs

class Student_jcs(Person_jcs):
    def __init__(self_jcs, name_jcs, age_jcs, course_jcs):
        super().__init__(name_jcs, age_jcs)
        self_jcs.course_jcs = course_jcs

    def display_student_jcs(self_jcs):
        print("Name:", self_jcs.name_jcs)
        print("Age:", self_jcs.age_jcs)
        print("Course:", self_jcs.course_jcs)

student1_jcs = Student_jcs("Maria", 20, "BSIS")
student1_jcs.display_student_jcs()
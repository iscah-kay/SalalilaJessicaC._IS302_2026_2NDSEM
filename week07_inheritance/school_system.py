class Person_jcs:
    def __init__(self_jcs, name_jcs, age_jcs):
        self_jcs.name_jcs = name_jcs
        self_jcs.age_jcs = age_jcs

    def display_info_jcs(self_jcs):
        print("Name:", self_jcs.name_jcs)
        print("Age:", self_jcs.age_jcs)

class Student_jcs(Person_jcs):
    def __init__(self_jcs, name_jcs, age_jcs, course_jcs):
        super().__init__(name_jcs, age_jcs)
        self_jcs.course_jcs = course_jcs

    def display_info_jcs(self_jcs):
        super().display_info_jcs()
        print("Course:", self_jcs.course_jcs)

class Teacher_jcs(Person_jcs):
    def __init__(self_jcs, name_jcs, age_jcs, subject_jcs):
        super().__init__(name_jcs, age_jcs)
        self_jcs.subject_jcs = subject_jcs

    def display_info_(self_jcs):
        super().display_info_jcs()
        print("Subject:", self_jcs.subject_jcs)

# Example usage
student_jcs = Student_jcs("Maria", 20, "BSIS")
teacher_jcs = Teacher_jcs("Mr. Smith", 45, "Mathematics")

print("Student Info:")
student_jcs.display_info_jcs()
print("\nTeacher Info:")
teacher_jcs.display_info_jcs()
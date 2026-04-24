name_jcs = input("Enter student name: ")
course_jcs = input("Enter course: ")
with open("students.txt", "a") as file_jcs:
    file_jcs.write(name_jcs + "," + course_jcs + "\n")

print("\nStudent Records")
with open("students.txt", "r") as file_jcs:
    for line_jcs in file_jcs:
        print(line_jcs.strip())

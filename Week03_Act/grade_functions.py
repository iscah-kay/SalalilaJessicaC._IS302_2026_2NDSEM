def calculate_average(grade1_jcs, grade2_jcs, grade3_jcs):
    """Calculate the average of three grades"""
    return (grade1_jcs + grade2_jcs+ grade3_jcs) / 3

def get_remark(average_jcs):
    """Return the remark based on the average grade"""
    if average_jcs >= 90:
        return "Excellent"
    elif average_jcs >= 85:
        return "Very Good"
    elif average_jcs >= 80:
        return "Good"
    elif average_jcs >= 75:
        return "Fair"
    else:
        return "Failed"

# Main program
print("----- STUDENT GRADE PROCESSOR -----")
student_name_jcs = input("Enter student name: ")
grade1_jcs = float(input("Enter first grade: "))
grade2_jcs = float(input("Enter second grade: "))
grade3_jcs = float(input("Enter third grade: "))

# Calculate average and get remark
average_jcs = calculate_average(grade1_jcs, grade2_jcs, grade3_jcs)
remark_jcs = get_remark(average_jcs)

# Display results
print("\n----- RESULTS -----")
print("Student Name:", student_name_jcs)
print("Grade 1:", grade1_jcs)
print("Grade 2:", grade2_jcs)
print("Grade 3:", grade3_jcs)
print("Average:", round(average_jcs, 2))
print("Remark:", remark_jcs)

print("----- GRADE LIST ANALYZER -----")
grades_jcs = []

# Ask user to enter 5 grades
for i_jcs in range(1, 6):
    grade_jcs = float(input(f"Enter grade {i_jcs}: "))
    grades_jcs.append(grade_jcs)

# Compute statistics
average_grade_jcs = sum(grades_jcs) / len(grades_jcs)
highest_grade_jcs = max(grades_jcs)
lowest_grade_jcs = min(grades_jcs)

# Display results
print("\n----- RESULTS -----")
print("Grades:", grades_jcs)
print("Average Grade:", round(average_grade_jcs, 1))
print("Highest Grade:", highest_grade_jcs)
print("Lowest Grade:", lowest_grade_jcs)

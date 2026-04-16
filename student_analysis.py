marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

total = sum(marks)
average = total / n
highest = max(marks)
lowest = min(marks)

print("\n--- Analysis Result ---")
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

print("\n--- Student Grades ---")

for i in range(n):
    if marks[i] >= 80:
        grade = "A"
    elif marks[i] >= 60:
        grade = "B"
    elif marks[i] >= 40:
        grade = "C"
    else:
        grade = "Fail"

    status = "Pass" if marks[i] >= 40 else "Fail"

    print(f"Student {i+1}: Marks = {marks[i]}, Grade = {grade}, Status = {status}")
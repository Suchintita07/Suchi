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
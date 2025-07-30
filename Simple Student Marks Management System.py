num_students = int(input("Enter number of students: "))
students = {}

for i in range(num_students):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\n--- Student Marks ---")
for name, marks in students.items():
    print(f"{name} : {marks}")

marks_list = list(students.values())
average = sum(marks_list) / num_students
highest = max(marks_list)
lowest = min(marks_list)

for name, marks in students.items():
    if marks == highest:
        topper = name
        break

print("\nAverage Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Topper:", topper)



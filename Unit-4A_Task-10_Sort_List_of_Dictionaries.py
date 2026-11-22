students = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "marks": marks})
print("Ascending order:")
print(sorted(students, key=lambda x: x["marks"]))
print("Descending order:")
print(sorted(students, key=lambda x: x["marks"], reverse=True))
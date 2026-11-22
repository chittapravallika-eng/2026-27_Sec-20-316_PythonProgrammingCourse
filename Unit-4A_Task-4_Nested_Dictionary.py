students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[roll] = {"name": name, "marks": marks}
print("Student Details:")
for roll, details in students.items():
    print("Name:", details["name"])
    print("Marks:", details["marks"])
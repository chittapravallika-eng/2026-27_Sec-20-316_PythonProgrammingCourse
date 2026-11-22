student = {
    "name": input("Enter student name: "),
    "marks": int(input("Enter marks: ")),
    "grade": input("Enter grade: ")
}
print("Student Record:")
for key, value in student.items():
    print(key, ":", value)
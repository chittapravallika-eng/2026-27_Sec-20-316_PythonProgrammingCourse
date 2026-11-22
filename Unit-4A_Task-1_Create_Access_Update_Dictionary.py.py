student = {
    "name": input("Enter name: "),
    "age": int(input("Enter age: ")),
    "course": input("Enter course: ")
}
student["age"] = int(input("Enter updated age: "))
student["city"] = input("Enter city: ")
print("Student Dictionary:", student)

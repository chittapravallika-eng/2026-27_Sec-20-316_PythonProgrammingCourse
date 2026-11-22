student = {
    "name": input("Enter name: "),
    "age": int(input("Enter age: ")),
    "course": input("Enter course: ")
}
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Get name:", student.get("name"))
student.update({"city": input("Enter city: ")})
print("After update:", student)
student.pop("age")
print("After pop:", student)
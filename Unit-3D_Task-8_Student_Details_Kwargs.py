def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
name = input("Enter student name: ")
python = int(input("Enter Python marks: "))
english = int(input("Enter English marks: "))
maths = int(input("Enter Maths marks: "))
student(name=name, Python=python, English=english, Maths=maths)
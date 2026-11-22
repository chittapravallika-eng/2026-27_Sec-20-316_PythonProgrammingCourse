marks = {}
n = int(input("Enter number of subjects: "))
for i in range(n):
    subject = input("Enter subject: ")
    mark = int(input("Enter marks: "))
    marks[subject] = mark
print("Keys:")
for key in marks:
    print(key)
print("Values:")
for value in marks.values():
    print(value)
print("Items:")
for key, value in marks.items():
    print(key, ":", value)
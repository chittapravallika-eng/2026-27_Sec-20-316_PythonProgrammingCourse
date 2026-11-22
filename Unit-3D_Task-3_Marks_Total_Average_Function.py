def calculate(a, b, c):
    total = a + b + c
    average = total / 3
    return total, average
a = int(input("Enter first subject marks: "))
b = int(input("Enter second subject marks: "))
c = int(input("Enter third subject marks: "))
t, avg = calculate(a, b, c)
print("Total:", t)
print("Average:", avg)
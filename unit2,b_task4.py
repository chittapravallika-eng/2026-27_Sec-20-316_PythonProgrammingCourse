n = int(input("Enter how many numbers: "))
largest = int(input("Enter number: "))
for i in range(n - 1):
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
print("Largest number =", largest)
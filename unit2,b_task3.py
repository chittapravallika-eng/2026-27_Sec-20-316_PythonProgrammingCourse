n = int(input("Enter how many numbers: "))
sum = 0
for i in range(n):
    num = int(input("Enter number: "))
    sum = sum + num
average = sum / n
print("Sum =", sum)
print("Average =", average)
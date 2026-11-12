a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))
total = a + b + c
if a > 0 and b > 0 and c > 0 and total == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
n = int(input("Enter a number between 1 and 100: "))
if n <= 1:
    print(n, "is Not a Prime Number")
else:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is Not a Prime Number")
            break
    else:
        print(n, "is a Prime Number")
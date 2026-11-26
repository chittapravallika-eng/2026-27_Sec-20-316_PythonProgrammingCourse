try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Please enter valid integers")
lst = list(map(int, input("Enter list elements: ").split()))
try:
    index = int(input("Enter index: "))
    print("Element:", lst[index])
except ValueError:
    print("Error: Enter a valid integer")
except IndexError:
    print("Error: Index out of range")
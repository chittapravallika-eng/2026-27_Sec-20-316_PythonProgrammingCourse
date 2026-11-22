x = int(input("Enter global variable value: "))
def show():
    x = int(input("Enter local variable value: "))
    print("Local variable:", x)
show()
print("Global variable:", x)
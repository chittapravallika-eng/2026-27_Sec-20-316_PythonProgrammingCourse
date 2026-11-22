balance = float(input("Enter initial balance: "))
def deposit(amount):
    global balance
    balance += amount
    print("Updated balance:", balance)
def show():
    balance = float(input("Enter local balance: "))
    print("Local balance:", balance)
amount = float(input("Enter deposit amount: "))
deposit(amount)
show()
print("Final bank balance:", balance)
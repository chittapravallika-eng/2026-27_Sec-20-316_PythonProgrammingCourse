count = 0
def increment():
    global count
    count += 1
    print("Counter:", count)
n = int(input("Enter number of times to increment: "))
for i in range(n):
    increment()
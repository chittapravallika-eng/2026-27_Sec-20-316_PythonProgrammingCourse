from functools import reduce
nums = list(map(int, input("Enter numbers: ").split()))
print("Squares:", list(map(lambda x: x*x, nums)))
print("Even numbers:", list(filter(lambda x: x%2 == 0, nums)))
print("Sum:", reduce(lambda x, y: x+y, nums))
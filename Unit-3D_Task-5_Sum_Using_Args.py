def total(*args):
    return sum(args)
nums = tuple(map(int, input("Enter numbers: ").split()))
print("Sum:", total(*nums))
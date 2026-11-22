def simple_interest(p, t, r=5):
    return (p * t * r) / 100
p = float(input("Enter principal: "))
t = float(input("Enter time: "))
print("Interest with default rate:", simple_interest(p, t))
print("Interest with explicit rate:", simple_interest(p, t, 10))
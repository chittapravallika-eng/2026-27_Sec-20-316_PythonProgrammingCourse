d1 = {"a": 10, "b": 20}
d2 = {"c": 30, "d": 40}
d3 = d1.copy()
d3.update(d2)
print("First dictionary:", d1)
print("Second dictionary:", d2)
print("Merged dictionary:", d3)
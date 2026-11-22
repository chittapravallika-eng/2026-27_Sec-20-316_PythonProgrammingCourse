lst = list(map(int, input("Enter list elements: ").split()))

lst.insert(1, int(input("Enter number to insert: ")))
print("After insert:", lst)

lst.append(int(input("Enter number to append: ")))
print("After append:", lst)

lst.remove(int(input("Enter number to remove: ")))
print("After remove:", lst)

lst.sort()
print("After sort:", lst)

lst.reverse()
print("After reverse:", lst)
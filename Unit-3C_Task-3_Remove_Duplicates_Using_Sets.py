lst = list(map(int, input("Enter list elements: ").split()))
new_list = list(set(lst))
print("Original list:", lst)
print("After removing duplicates:", new_list)
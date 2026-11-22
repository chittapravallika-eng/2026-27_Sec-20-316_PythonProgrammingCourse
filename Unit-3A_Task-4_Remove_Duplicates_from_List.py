lst = list(map(int, input("Enter list elements: ").split()))
new_list = []
for i in lst:
    if i not in new_list:
        new_list.append(i)
print("Original list:", lst)
print("List after removing duplicates:", new_list)
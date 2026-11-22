r = int(input("Enter rows: "))
c = int(input("Enter columns: "))
A = []
B = []
print("Enter first matrix:")
for i in range(r):
    A.append(list(map(int, input().split())))
print("Enter second matrix:")
for i in range(r):
    B.append(list(map(int, input().split())))
print("Addition:")
for i in range(r):
    for j in range(c):
        print(A[i][j] + B[i][j], end=" ")
    print()
print("Subtraction:")
for i in range(r):
    for j in range(c):
        print(A[i][j] - B[i][j], end=" ")
    print()
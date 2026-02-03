# Two Star Patterns in One Program

n1 = int(input("Enter rows for Pattern 1: "))
n2 = int(input("Enter rows for Pattern 2: "))

print("\nPattern 1:")
for i in range(1, n1 + 1):
    print("* " * i)

print("\nPattern 2:")
for i in range(1, n2 + 1):
    for j in range(i):
        print("*", end=" ")
    print()

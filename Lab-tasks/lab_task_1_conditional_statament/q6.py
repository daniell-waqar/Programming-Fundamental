x = int(input("enter size: "))
y = int(input("enter size: "))
z = int(input("enter size: "))
if x == y == z:
    print("equilateral triangle")
elif x == y != z or x != y == z or x == z != y:
    print("isoceles triangle")
else:
    print("scalene trianle")

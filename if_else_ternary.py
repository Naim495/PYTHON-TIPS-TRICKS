a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

biggest = a if (a > b and a > c) else b if b > c else c
print(f"The biggest number is {biggest}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("The biggest number is", a)
elif b >= a and b >= c:
    print("The biggest number is", b)
else:
    print("The biggest number is", c)

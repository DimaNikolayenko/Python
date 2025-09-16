
a = int(input("Enter a (1-100): "))
while a < 1 or a > 100:
    a = int(input("Enter a again (1-100): "))

b = int(input("Enter b (1-100): "))
while b < 1 or b > 100:
    b = int(input("Enter b again (1-100): "))

if a > b:
    x = a + a - b
elif a == b:
    x = -a
else:
    x = (a * b - 1) / b

print("Result:", x)

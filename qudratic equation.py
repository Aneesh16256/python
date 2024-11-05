a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    x1 = (-b + discriminant**0.5) / (2*a)
    x2 = (-b - discriminant**0.5) / (2*a)
    print("first real and distinct solutions: x1 =", "+", x1)
    print("second real and distinct solutions: x1 =", "+", x2)
elif discriminant == 0:
    x1 = -b / (2*a)
    print(x1)
else:
    real_part = -b / (2*a)
    imaginary_part = (-discriminant**0.5) / (2*a)
    print("first complex solutions: x1 = ", real_part ,"+", imaginary_part,"+i")
    print("second complex solution: x2 = ", real_part ,"-", imaginary_part,"+i")
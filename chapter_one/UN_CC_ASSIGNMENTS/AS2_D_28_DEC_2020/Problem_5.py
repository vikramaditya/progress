# Problem 5

print("The angle a is :")
a = int(input())

print("The angle b is :")
b = int(input())

print("The angle c is :")
c = int(input())

if a + b + c == 180:
    pass

else:
    print("Angle Values not Valid for a Triangle")

if (a< 90 and b <90 and c <90) and a + b + c == 180:
    print("Acute Angle Triangle")
else:
    pass

if (a == 90 and b + c == 90) or (b == 90 and a + c ==90) or (c == 90 and a + b == 90):
    print("Right Angled Triangle")
else:
    pass

if (a> 90 and b + c <90 and a + b + c == 180) or (b>90 and a + c <90 and a + b + c == 180) or (c> 90 and a + b <90 and a + b + c == 180):
    print("Obtuse Angled Triangle")

# ALL OK
# Problem 3

print("Enter the 4 integers")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))

print("Largest integer entered is: ")

if a > b and a > c and a > d:
    maximum_number = a
else:
    pass

if b > c and b > a and b > d:
    maximum_number = b
else:
    pass

if c > b and c > a and c > d:
  maximum_number = c
else:
    pass

if d > b and d > c and d > a:
   maximum_number = d

print(maximum_number)

# All OK
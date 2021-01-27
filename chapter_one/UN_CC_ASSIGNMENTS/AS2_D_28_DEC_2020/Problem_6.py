# Problem 6

print("Enter the Perimeter: ")
peri = int(input())

print("Enter the Area: ")
area = int(input())

print("First Approach - AM-GM Relation")

if peri >= 4*(area**0.5):
    print("Rectangle Exists")
else:
    print("Rectangle Does not Exist")

print ("Second Approach - Quadratic Equation")

if peri * peri >= 16 * area:
    print("Rectangle Exists")
else:
    print("Rectangle Does not Exist")

# Still Some Doubt. Come Here Later :)

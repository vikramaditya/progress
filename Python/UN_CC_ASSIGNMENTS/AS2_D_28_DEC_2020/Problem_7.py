# Problem 7

t = int(input("Value of t is: "))

s = int(input("Value of s is: "))

u = int(input("Value of u is: "))

t = t % (2*s + 2*u)

if t<s:
    print("red")
else:
    print("yellow")

if (t >= s+u) and (t < 2 * s+u):
    print("green")
else:
    pass

# Double Check Needed

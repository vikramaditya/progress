# Problem 9

x = int(input("Value of x is: "))

x = x%4

print("Value of (3**x)%10 is:")
if x == 0:
    print("1")
else:
    pass

if x == 1:
    print("3")
else:
    pass

if x == 2:
    print("9")
else:
    pass

if (x != 0) and (x != 1) and (x != 2):
    print("7")

# All OK

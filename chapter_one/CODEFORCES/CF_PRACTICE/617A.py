x = int(input())

y = x//5


if x % 5 > 0:
    y += 1
    x -= 1
    
print(y)
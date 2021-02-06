# https://www.codechef.com/PEC2021B/problems/LINPAT

def clara(lana):
    zara = 1
    sara = 1
    if lana == 1:
        print(10)
    while zara <= lana/2:
        print(zara * 10, end=" ")
        print(sara * 2, end=" ")
        zara +=1
        sara += 1

jane = int(input())
clara(jane)

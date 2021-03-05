# https://www.codechef.com/PEC2021B/problems/ISGOODNM

def good_boi(doge):
    rex = 0
    tiger = 1
    while tiger <= (doge ** 0.5):
        if (doge % tiger == 0):
            if (doge / tiger == tiger):
                rex += 1
            else:
                rex += tiger + doge/tiger
        tiger += 1
    rex -= doge

    if rex == tommy:
        print("YES")
    else:
        print("NO")

tommy = int(input())
good_boi(tommy)

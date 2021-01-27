# https://www.codechef.com/INPRG01/problems/NUMPLIN
clara = input()


for i in range(0, int(len(clara)/2)):
        if clara[i] != clara[len(clara)-i-1]:
            res = "NO"
        else:
            res = "YES"
print(res)

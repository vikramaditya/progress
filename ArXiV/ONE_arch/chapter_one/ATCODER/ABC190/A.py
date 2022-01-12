# include the url here
A, B, C = [int(A) for A in input().split()]

if (C == 1) and A == B:
    print("Takahashi")
    quit()

if C == 0:
    while A > 0 or B > 0:
        A -= 1
        B -= 1

if C == 1:
    while A > 0 or B > 0:
        B -= 1
        A -= 1



if A > B:

    print("Takahashi")

else:
        print("Aoki")

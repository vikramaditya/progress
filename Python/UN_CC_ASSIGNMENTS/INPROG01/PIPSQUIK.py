# https://www.codechef.com/INPRG01/problems/CATSDOGS
T = int(input())

while T > 0:
    (N, H, Y1, Y2, L) = map(int,input().split())

    count = 0

    while N > 0:
        (TI,XI)= map(int,input().split())

        if TI == 1 and XI >= H -Y1 and L > 0:
            count = count + 1
        
        if TI == 1 and XI < H -Y1 and L >= 1:
            L = L -1
            if L == 0:
                pass
            else:
                count = count + 1
        
        if TI == 2 and XI >= H - Y2 and L > 0:
            count = count + 1
        
        if TI == 2 and XI < H - Y2 and L >= 1:
            L = L - 1
            if L == 0:
                pass
            else:
                count = count + 1
        N  = N - 1
    T = T - 1
    print(count)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License

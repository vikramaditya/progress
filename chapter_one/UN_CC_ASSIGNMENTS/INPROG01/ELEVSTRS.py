# https://www.codechef.com/INPRG01/problems/ELEVSTRS

c = int(input())

while c > 0:
    N, V, J = [int(N) for N in input().split()]

    t_el = N / V

    X = N * 2 ** 0.5

    t_st = X / J

    if t_el > t_st:
        print("Elevator")
    else:
        print("Stairs")

    c = c - 1

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License

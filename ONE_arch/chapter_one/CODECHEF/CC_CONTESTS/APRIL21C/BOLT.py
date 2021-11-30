t = int(input())
for i in range(t):
    k1, k2, k3, v = [float(c) for c in input().split()]

    final_speed = k1 * k2 * k3 * v

    race_speed = 100 / final_speed

    race_speed = format(race_speed, ".2f")
    race_speed = float(race_speed)

    if race_speed < 9.58:
        print("YES")
    else:
        print("NO")

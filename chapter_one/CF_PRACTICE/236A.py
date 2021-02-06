# https://codeforces.com/problemset/problem/236/A

jane = input()
jane = list(jane)

jane = list(dict.fromkeys(jane))

if len(jane) == 1 or len(jane) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print('IGNORE HIM!')

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License

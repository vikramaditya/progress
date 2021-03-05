j = int(input())
for j in range(j):
    ls = input()
    y = [int(x) if x.isdigit() else x
          for z in ls for x in str(z)]
    print(y[0] + y[-1])
    
# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License

# https://www.codechef.com/PEC2021/problems/FDGHLM

clara, jane = [int(n) for n in input().split()]

shizuka = clara * jane

while (clara):
	lana = clara
	clara = jane % clara
	jane = lana

print(jane, shizuka//jane)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License

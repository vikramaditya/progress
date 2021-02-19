# https://www.codechef.com/PEC2021D/problems/MXOVRLP
# There are idiots and there are dumb people, and, then, there's me.

def MXOVERLP(arr):
	temp = 0
	i = 0
	input_list = []
	for g in range(len(arr)):
		input_list.append([arr[g][0], '-1'])
		input_list.append([arr[g][1], '-2'])

	input_list = sorted(input_list)

	for g in range(len(input_list)):
		if (input_list[g][1] == '-1'):
			i += 1
		
		if (input_list[g][1] == '-2'):
			i -= 1
		
		temp = max(temp, i)
	return temp

t = int(input())

for g in range(0,t):
	n = int(input())
	m = int(input())
	arr = []
	for f in range(0,n):
		
		l,r = [int(c) for c in input().split()]
		arr.append([l, r])

	print(MXOVERLP(arr))
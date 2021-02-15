# https://www.codechef.com/PEC2021D/problems/SETGEN

def power_set(arr, n):
    elements = []

    for i in range(2**n):
        sub_set = ''    # Here we have initialised an empty string
        for j in range(n):
            if (i & (1 << j)) != 0:
                sub_set += str(arr[j]) + "-1"
        if sub_set not in elements and len(sub_set) > 0:
            elements.append(sub_set)
    for sub_set in elements:
        arr = sub_set.split('-1')
        for string in arr:
            print(string, end = " ")
        print("")

t = int(input())

for g in range(0,t):
    number_set = []
    go = int(input())

    for d in range(1,go+1):
        number_set.append(d)

    power_set(number_set, len(number_set))

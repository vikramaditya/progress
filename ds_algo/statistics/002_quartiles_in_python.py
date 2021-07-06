"""
Author: valisport
Calculating Quartiles of a given array
Check:  https://en.wikipedia.org/wiki/Quartile
v0.1 ==> add documentation
"""

def get_median(arr):
    n = len(arr)
    index = n // 2

    if n % 2:
        median = sorted(arr)[index]
    else:
        median = sum(sorted(arr)[index -1:index+1]) // 2

    return median

def quartiles(arr):
    n = len(arr)

    if n % 2 == 0:
        median = get_median(arr)
        indx = n//2
        q1 = arr[0:indx+1]
        med_q1 = get_median(q1)
        q3 = arr[indx:]
        med_q3 = get_median(q3)
    else:
        median = get_median(arr)
        indx = arr.index(median)
        q1 = arr[0:indx]
        med_q1 = get_median(q1)
        q3 = arr[indx+1:]
        med_q3 = get_median(q3)

    print(med_q1)
    print(median)
    print(med_q3)



n = int(input())
arr = [int(c) for c in input().split()]
arr.sort()

quartiles(arr)

"""
Computing / Finding the mean, the median, and the mode in Python
v0.1 => to be polished
"""
n = int(input()) # total number of items in the list
go = [int(c) for c in input().split()] # the list

mean = sum(go) / n # finding mean

index = n // 2 # finding index of the possible median(s)

if n % 2: # finding median - if n is even, locating the two middle values
    median = sorted(go)[index]
else: # if n is odd, slice and get two values
    median = sum(sorted(go)[index - 1:index + 1]) / 2

from collections import Counter # importing the Counter class which gives most_common function

c = Counter(go) # short code == better code

modes = [i for i, j in c.items() if j == c.most_common(1)[0][1]]    # count the observations, create a list with observations occuring same no. of times
# Since .most_common(1) returns a list with one tuple of the form (observation, count), we need to get the observation at index 0 in the list and then the item at index 1 in the nested tuple. This can be done with the expression c.most_common(1)[0][1]. That value is the first mode of our sample.

modes.sort() # Every number occurs once, making 1 the maximum number of occurrences for any number in go(input_list). Because we have multiple values to choose from, we want to select the smallest one.

print(mean)
print(median)
print(modes[0])


# https://www.codechef.com/PEC2021C/problems/TOLLCNT

from math import ceil

n = int(input())
en_time = {}
ex_time = {}
time_val = []
for d in range(0,n):
    entry_or_exit = str(input())
    keys = input()
    values = int(input())
    time_val.append(keys)

    if entry_or_exit == "entry":
        en_time[keys] = values
    else:
        ex_time[keys] = values

time_val.sort()
toll = 0
for g in range(0, n, 2):
    ent_time = en_time[time_val[g]]
    ext_time = ex_time[time_val[g]]

    raw_time = (ext_time - ent_time) / 60
    time = ceil(raw_time)
    toll += 60 + (time-1) * 30

print(toll)

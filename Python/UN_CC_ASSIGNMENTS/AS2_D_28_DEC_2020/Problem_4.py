# Problem 4

print("What's the year?")
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    year_is = ("leap_year")
else:
    year_is = ("not_leap_year")

print(year_is)

# All OK
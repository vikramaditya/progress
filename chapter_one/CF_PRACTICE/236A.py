jane = input()
jane = list(jane)

jane = list(dict.fromkeys(jane))

if len(jane) == 1 or len(jane) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print('IGNORE HIM!')

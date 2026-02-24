username = input()

uniqueSize = len(set(username))

if uniqueSize % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")


username = input()

unique = len(set(username))

if unique % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")



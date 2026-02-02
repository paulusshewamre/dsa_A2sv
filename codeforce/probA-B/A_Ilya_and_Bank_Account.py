balance = input()


if int(balance) > 0:
    print(balance)
else:
    removeLast = int(balance[:-1])
    removeSLast = int(balance[:-2] + balance[-1])
    print(max(removeLast, removeSLast))
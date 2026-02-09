t = int(input())

for i in range(t):
    n = int(input())
    turnA = True
    colA = 0
    colB = 0
    while n > 0:
        if n - 3 > 0 and turnA:
            colA += 3
            n -= 3
        elif n - 3 > 0 and not turnA:
            colB += 3
            n -= 3
        elif n - 2 > 0 and turnA:
            colA += 2
            n -= 2
        else:
            colB += 2
            n -= 2
        turnA = not turnA
        print(colA, colB)
    print(abs(colA - colB))
        
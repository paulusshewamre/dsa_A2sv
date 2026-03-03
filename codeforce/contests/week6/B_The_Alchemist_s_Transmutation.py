t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    y = int(input())
    smallerNums = False
    greateNums = False
    for i in range(n):
        if a[i] <= y:
            smallerNums = True
        if a[i] >= y:
            greateNums = True
    if smallerNums and greateNums:
        print("YES")
    else:
        print("NO")
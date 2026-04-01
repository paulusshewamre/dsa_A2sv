t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    x1, y1 = map(int, input().split())
    if x > y and x1 > y1:
        print("YES")
    elif x < y and x1 < y1:
        print("YES")
    else:
        print("NO")
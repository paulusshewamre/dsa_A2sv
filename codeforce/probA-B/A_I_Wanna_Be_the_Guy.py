target = int(input())

xPass = list(map(int, input().split()))
yPass = list(map(int, input().split()))

levels = set(xPass[1:] + yPass[1:])

if len(levels) == target:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
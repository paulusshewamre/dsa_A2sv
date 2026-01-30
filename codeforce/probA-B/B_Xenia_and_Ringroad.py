n, m = map(int, input().split())
tasks = list(map(int, input().split()))

cur = 1
time = 0

for target in tasks:
    if target >= cur:
        time += target - cur
    else:
        time += (n - cur) + target
    cur = target

print(time)
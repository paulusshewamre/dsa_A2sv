n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

pl = 0
p2 = 0
res = []
while pl < n and p2 < m:
    if arr1[pl] < arr2[p2]:
        res.append(arr1[pl])
        pl += 1
    else:
        res.append(arr2[p2])
        p2 += 1

while pl < n:
    res.append(arr1[pl])
    pl += 1

while p2 < m:
    res.append(arr2[p2])
    p2 += 1

print(*res)
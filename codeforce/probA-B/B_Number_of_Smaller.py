n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

res = []
first = 0
for second in range(m):
    while first < n and arr1[first] < arr2[second]:
        first += 1
    res.append(first)

print(*res)

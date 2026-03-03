t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    res = float('inf')

    for i in range(n - 2):
        cost = (arr[i+1] - arr[i]) + (arr[i+2] - arr[i+1])
        res = min(res, cost)

    print(res)
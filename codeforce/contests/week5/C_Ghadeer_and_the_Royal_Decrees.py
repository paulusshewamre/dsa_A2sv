t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    res = [0] * n
    for i in range(m):
        c , l , r = input().split()
        l = int(l) 
        r = int(r) 
        for j in range(len(arr)):
            if arr[j] >= l and arr[j] <= r:
                if c == "+":
                    arr[j] += 1
                else:
                    arr[j] -= 1
        res[i] = max(arr)

    print(*res)

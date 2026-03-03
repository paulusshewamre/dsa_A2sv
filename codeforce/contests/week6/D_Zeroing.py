n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

total_sub = 0
i = 0  

while k > 0:
    while i < n and arr[i] - total_sub == 0:
        i += 1

    if i == n:
        print(0)
        k -= 1
        continue

    smallest_val = arr[i] - total_sub
    print(smallest_val)

    total_sub += smallest_val

    k -= 1
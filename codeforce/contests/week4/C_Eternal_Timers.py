t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    smallest_value = min(arr)
    smallest_indexes = [i for i, x in enumerate(arr) if x == smallest_value]

    for i in range(len(smallest_indexes)):
        time = 2 * (n-1-smallest_indexes[i])
        if smallest_value - time < 1:
            print("NO")
            break
    else:
        print("YES")
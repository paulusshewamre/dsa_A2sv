t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    count = 0

    if total % n != 0:
        count = -1
    else:
        average = total // n
        for val in arr:
            if val > average:
                count+=1
    print(count)
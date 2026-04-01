t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    crowd_sum = arr[0] + arr[1]
    elite_sum = arr[-1]
    countCrowd = 2
    countElite = 1
    l = 1
    r = len(arr) - 1
    flag = False
    while l < r:
        if elite_sum > crowd_sum and countElite < countCrowd:
            flag = True
            break
        if crowd_sum <= elite_sum:
            l += 1
            if l >= r:
                break
            crowd_sum += arr[l]
            countCrowd += 1
        else:
            r -= 1
            if l >= r:
                break
            elite_sum += arr[r]
            countElite += 1

    if elite_sum > crowd_sum and countElite < countCrowd:
        flag = True

    if flag:
        print("YES")
    else:
        print("NO")
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    max_num = max(a)
    count_max = a.count(max_num)
    if count_max % 2 != 0:
        print("YES")
    else:     
        print("NO")
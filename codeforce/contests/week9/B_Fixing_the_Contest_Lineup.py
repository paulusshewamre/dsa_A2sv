t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p1 , p2 = 0, 0
    cnt = 0
    while p1 < n-cnt and p2 < n:
        if a[p1] > b[p2]:
            p2+=1
            cnt+=1
        else:
            p1+=1
            p2+=1
    print(cnt)
    

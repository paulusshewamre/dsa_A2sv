t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    p = [0]*n
    ok = True
    i = 0
    
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        
        if j - i == 1:
            ok = False
            break
        
        
        for k in range(i, j):
            if k == j-1:
                p[k] = i
            else:
                p[k] = k+1
        
        i = j
    

    if not ok:
        print(-1)
    else:
        print(*[x+1 for x in p])


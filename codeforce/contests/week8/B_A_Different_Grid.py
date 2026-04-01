t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    res = []

    for i in range(n):
        row = list(map(int, input().split()))
        res.append(row)
            
    if n*m == 1:
        print(-1)
        continue
    
    if m == 1:
        row = res[n-1]
        print(*row)
        i = 0
        while i < n-1:
            col = res[i]
            print(*col)
            i+=1
        continue
    
    
    for i in range(n): 
        row = res[i]
        row = row[1:] + [row[0]]
        print(*row)
    
    
    


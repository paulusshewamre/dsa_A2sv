t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    
    cnt = 0
    lastOncePosition = -k 
    
    for i in range(n):
        if s[i] == '1':
            if i - lastOncePosition >= k:
                cnt += 1
                lastOncePosition = i
            else:
                lastOncePosition = i
    
    print(cnt)
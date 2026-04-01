n, m = map(int, input().split())

L, R = 1, n

for _ in range(m):
    clue = input().split()
    
    direction = clue[2]
    i = int(clue[-1])
    
    if direction == "left":
        R = min(R, i - 1)
    else:
        L = max(L, i + 1)

if L > R:
    print(-1)
else:
    print(R - L + 1)
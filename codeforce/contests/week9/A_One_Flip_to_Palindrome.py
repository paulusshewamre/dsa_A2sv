t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    misMatchIndex = []
    
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            misMatchIndex.append(i)
    
    if not misMatchIndex:
        print("Yes")
        continue
    
    if misMatchIndex[-1] - misMatchIndex[0] + 1 == len(misMatchIndex):
        print("Yes")
    else:
        print("No")
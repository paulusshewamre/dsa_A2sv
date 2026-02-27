
from collections import defaultdict

t = int(input())

for _ in range(t):
    n , m = map(int, input().split())
    myMap = defaultdict(int)
    for i in range(n):
        arr = list(map(int, input().split()))
        arr.sort()
        for i in range(1,len(arr)):
            if arr[i-1]+1 == arr[i]:
                print(-1)
                exit(1)
        if len(myMap) <= n:
            myMap[min(arr)] = i + 1
    print(*myMap.values())
    

    
        

from collections import Counter

t = int(input())

for _ in range(t):
    n, c, d = map(int, input().split())
    nums = list(map(int, input().split()))
    
    start = min(nums)
    
    expected = [start + i*c + j*d for i in range(n) for j in range(n)]
    
    if Counter(expected) == Counter(nums):
        print("YES")
    else:
        print("NO")
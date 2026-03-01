t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print("YES")
        break
    arr.sort()
    i = 0
    j = n-1
    while i < j:
        if abs(arr[i] - arr[j]) > 1:
            print("NO")
            break
        elif abs(arr[i] - arr[j]) <= 1:
            if arr[i] < arr[j]:      
                i+=1
            else:
                j-=1
        print("YES")
        break
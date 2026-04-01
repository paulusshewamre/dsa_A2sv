t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = False
    for i in range(n):
        j = i+1
        k = n-1
        while j < k and not flag:
            if arr[i] < arr[j] and arr[j] > arr[k]:
                print("YES")
                print(i+1,j+1,k+1)
                flag = True
                break
            j+=1  
    if not flag:
        print("NO")
    
    

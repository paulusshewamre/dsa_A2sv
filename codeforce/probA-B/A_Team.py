n = int(input())
count = 0
for i in range(n):
    sum = 0
    a,b,c = map(int, input().split())
    sum = a + b + c
    if sum > 1:
        count+=1

print(count)
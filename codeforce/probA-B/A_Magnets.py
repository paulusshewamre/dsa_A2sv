n = int(input())

count = 0
prev = ""
for i in range(n):
    magnet = input()
    if prev != magnet:
        count+=1
        prev = magnet
    
print(count)
from collections import defaultdict
n = int(input())


counter = defaultdict(int)
for i in range(n):
    m = int(input())
    for j in range(m):
        message = input()
        counter[message] += 1        
        

max_count = max(counter.values())
rcr = (max_count / n) * 100
if rcr >= 80:
    print("YES")
else:
    print("NO")


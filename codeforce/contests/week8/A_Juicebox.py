import random
big = random.randint(1000, 10 ** 6)

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    total = 0
    counter = {}
    for i in range(k):
        b, c = map(int, input().split())
        counter[b^big] = counter.get(b^big, 0) + c  
    sorted_counter = sorted(counter.values(), key=lambda x: x, reverse=True)
    i = 0
    while i < len(sorted_counter) and n > 0:
        total += sorted_counter[i]
        n -= 1
        i += 1
    print(total)
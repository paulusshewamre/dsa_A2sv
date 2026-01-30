n = int(input())
pages = list(map(int, input().split()))

day = 0
 
while n > 0:
    n -= pages[day]
    day = (day + 1) % 7

print(day if day != 0 else 7)
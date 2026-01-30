n = int(input())
cards = list(map(int, input().split()))

sum1, sum2 = 0, 0
start, end = 0, len(cards)-1
turnA = True

while start <= end:
    largest = 0
    if cards[start] >= cards[end]:
        largest = cards[start]
        start += 1
    else:
        largest = cards[end]
        end -= 1
    if turnA:
        sum1 += largest
        turnA = False
    else:
        sum2 += largest
        turnA = True

print(sum1, sum2)
    


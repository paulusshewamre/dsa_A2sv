n = int(input())
cards = list(map(int, input().split()))

sereja_score = 0
dima_score = 0

p1 = 0
p2 = n - 1

sereja_turn = True
while p1 <= p2:
    if cards[p1] > cards[p2]:
        if sereja_turn:
            sereja_score += cards[p1]
        else:
            dima_score += cards[p1]
        p1 += 1
    else:
        if sereja_turn:
            sereja_score += cards[p2]
        else:
            dima_score += cards[p2]
        p2 -= 1

    sereja_turn = not sereja_turn

print(sereja_score, dima_score)
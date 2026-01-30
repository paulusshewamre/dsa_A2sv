n , m = map(int, input().split())
prices = list(map(int, input().split()))

profit = 0
for price in prices:
    if price < 0:
        profit += abs(price)
    
print(profit)
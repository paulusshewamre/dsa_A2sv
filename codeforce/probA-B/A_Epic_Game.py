import math
a, b , n = map(int, input().split())

turnA = True
while True:
    if turnA:
        gcd = math.gcd(a, n)
    else:
        gcd = math.gcd(b, n)
    
    if gcd > n:
        print(1 if turnA else 0)
        break

    n -= gcd
    turnA = not turnA



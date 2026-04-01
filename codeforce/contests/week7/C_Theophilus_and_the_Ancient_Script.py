t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    b = 0
    ans = 0

    for c in reversed(s):
        if c == 'B':
            b += 1
        else:
            if b > 0:
                ans += b
                b -= 1

    print(ans)
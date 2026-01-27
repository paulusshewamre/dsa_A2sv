n = int(input())

for _ in range(n):
    exp = input()
    a, b = exp.split('+')
    a, b = int(a), int(b)
    print(a + b)

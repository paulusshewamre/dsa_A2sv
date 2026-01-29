n = int(input())

res = 0
for i in range(n):
    exp = input()
    if exp[1] == '+':
        res+=1
    else:
        res -= 1

print(res)
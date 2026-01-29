n, k = map(int, input().split())
score = list(map(int, input().split()))
passed = 0
threshold = score[k-1]

for i in range(n):
    if score[i] >= threshold and score[i] > 0:
        passed += 1
    else:
        break

print(passed)

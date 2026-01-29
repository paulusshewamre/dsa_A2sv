n, h = map(int, input().split())
friendsHight = list(map(int, input().split()))

width = n
for num in friendsHight:
    if num > h:
        width += 1

print(width)
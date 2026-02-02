n = int(input())
word = input()

size = len(set(word))

if size < 26:
    print("NO")
else:
    print("YES")
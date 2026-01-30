n = int(input())
word = input().lower()

if n < 26:
    print("NO")
else:
    unique = set(word)
    if len(unique) < 26:
        print("NO")
    else:
        print("YES")

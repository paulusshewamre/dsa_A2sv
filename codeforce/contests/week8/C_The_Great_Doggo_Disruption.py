n = int(input())
s = input().strip()

s = sorted(s)
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        print("Yes")
        exit()
print("No")
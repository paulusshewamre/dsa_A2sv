n = int(input())
s = input()
res = 10**9

start = 0
end = 3

while end < n:
    diff = 0
    diff += min(abs(ord(s[start]) - ord('A')), 26 - abs(ord(s[start]) - ord('A')))
    diff += min(abs(ord(s[start + 1]) - ord('C')), 26 - abs(ord(s[start + 1]) - ord('C')))
    diff += min(abs(ord(s[start + 2]) - ord('T')), 26 - abs(ord(s[start + 2]) - ord('T')))
    diff += min(abs(ord(s[start + 3]) - ord('G')), 26 - abs(ord(s[start + 3]) - ord('G')))

    res = min(res, diff)
    start += 1
    end += 1

print(res)

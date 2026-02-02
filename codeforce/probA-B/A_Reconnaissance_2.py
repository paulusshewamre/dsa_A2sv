n = int(input())
heights = list(map(int, input().split()))

res = [1,2]
minDif = abs(heights[1]-heights[0])

for i in range(1,n):
    diff = abs(heights[i]-heights[i-1])
    if diff < minDif:
        minDif = diff
        res = [i, i+1]


diff = abs(heights[n-1] - heights[0])
if minDif > diff:
    res = [n, 1]

print(res[0], res[1])

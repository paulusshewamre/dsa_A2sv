w , t = map(int, input().split())
n = int(input())
flag = False
for i in range(n):
    a , b = map(int, input().split())
    if a >= w and b < t:
        flag = True

if flag:
    print("The Fallen Champion")
else:
    print("The Champion Saves the Accused")
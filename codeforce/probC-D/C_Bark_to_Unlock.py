password = input()
n = int(input())

foundLeft = False
foundRight = False

for _ in range(n):
    attempt = input()
    if attempt == password:
        print("YES")
        exit()
    if attempt[0] == password[1]:
        foundRight = True
    if attempt[1] == password[0]:
        foundLeft = True

if foundLeft and foundRight:
    print("YES")
else:
    print("NO")

matrix = [ list(map(int, input().split())) for i in range(5)]


for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            res = abs(2-i)+abs(2-j)
            print(res)
            exit()
    




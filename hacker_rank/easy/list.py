if __name__ == '__main__':
    N = int(input())
    items = []
    for i in range(N):
        line = input().split()
        cmd = line[0]
        
        if cmd == "insert":
            items.insert(int(line[1]), int(line[2]))
        elif cmd == "append":
            items.append(int(line[1]))
        elif cmd == "pop":
            items.pop()
        elif cmd == "remove":
            items.remove(int(line[1]))
        elif cmd == "sort":
            items.sort()
        elif cmd == "reverse":
            items.reverse()
        else:
            print(items)
        
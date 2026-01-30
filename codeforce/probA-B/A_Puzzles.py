s, n = map(int, input().split())
puzzles = list(map(int, input().split()))

puzzles.sort()

start = 0
end = s-1

smallest = puzzles[end] - puzzles[start]



while end < len(puzzles):
    smallest = min(smallest, puzzles[end] - puzzles[start] )
    end += 1
    start += 1

print(smallest)
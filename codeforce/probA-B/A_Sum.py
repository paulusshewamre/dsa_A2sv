n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    largest = max(nums)
    nums.remove(largest)

    if sum(nums) == largest:
        print("YES")
    else:
        print("NO")
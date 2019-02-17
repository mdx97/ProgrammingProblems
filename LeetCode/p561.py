def arrayPairSum(nums):
    nums.sort()
    total = 0
    for i in range(0, len(nums), 2):
        total += nums[i]
    return total 

print(arrayPairSum([1, 4, 3, 2, 5, 7]))

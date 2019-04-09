# Naive Solution: For each "slot" i in the array, take the product of all numbers from the original array except the number at i.
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def exclusive_product(arr):
    n = len(arr)
    new = [0 for x in range(n)]
    for i in range(n):
        product = 1
        for j in range(n):
            if j != i:
                product *= arr[j]
        new[i] = product
    return new

# Solution: Take the product of the entire array. (P) For each "slot" i, set arr[i] = P / arr[i]
# Time Complexity: O(n)
# Space Complexity: O(1)
# Caveat: This solution does not work with 0s. 
def exclusive_product2(arr):
    total_product = 1
    for x in arr:
        total_product *= x
    for i in range(len(arr)):
        arr[i] = int(total_product / arr[i])
    return arr

# Solution: Build up a "forward product" array and a "backwards product" array. Each array simply stores the intermediary product of the entire array after multiplying by arr[i] either going forward (0 -> n) or backward (n -> 0).
# Time Complexity: O(n)
# Space Complexity: O(n)
# Notes:
# [1,2,3,4,5]
# i = 2
# product -> i from 0 = 2
# product -> i from n = 20
# p1 = [1, 2, 6, 24, 120]
# p2 = [120, 120, 60, 20, 5]
# new[i] = p1[i - 1] + p2[i + 1]
def exclusive_product3(arr):
    n = len(arr)
    p1 = [0 for x in range(n)]
    p2 = [0 for x in range(n)]
    
    prod = 1 
    for i in range(n):
        prod *= arr[i]
        p1[i] = prod
    
    prod = 1
    for i in range(n - 1, -1, -1):
        prod *= arr[i]
        p2[i] = prod

    new = [0 for x in range(n)]
    for i in range(n):
        total = 1 
        if i > 0:
            total *= p1[i - 1]
        if i < n - 1:
            total *= p2[i + 1]
        new[i] = total

    return new

print(exclusive_product3([1,2,3,4,5]))
print(exclusive_product3([3,2,1]))
print(exclusive_product3([3,2,1,0]))

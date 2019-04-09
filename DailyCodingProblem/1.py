"""
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""
# Naive Solution: Check every pair, return true if the sum of the pair is equal to k.
# Time Complexity: O(n * n/2) = O(n^2)
# Space Complexity: O(1)
def pair_sum_naive(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                return True
    return False

print(pair_sum_naive([1, 2, 3], 4))
print(pair_sum_naive([1, 2], 4))

# Solution: Create a set with all the elements in arr. Iterate through arr and check if k - arr[i] in the set.
# Time Complexity: O(n)
# Space Complexity: O(n)
def pair_sum_set(arr, k):
    elements = set(arr)
    for x in arr:
        diff = k - x
        if diff in elements and diff != x:
            return True
    return False

print(pair_sum_set([1, 2, 3], 4))
print(pair_sum_set([1, 2], 4))

# Solution: Same as above, but instead of creating a set out of all the elements before the loop, simply add each element to the set as we find them.
# Same Time and Space Complexity.
def pair_sum_set_one_pass(arr, k):
    elements = set()
    for x in arr:
        diff = k - x
        if diff in elements and diff != x:
            return True
        elements.add(x)
    return False

print(pair_sum_set_one_pass([1, 2, 3], 4))
print(pair_sum_set_one_pass([1, 2], 4))

# Solution: Sort array. Walk high and low pointers inwards checking the sum at each iteration.
# Time Complexity: O(n log(n))
# Space Complexity: O(1)
def pair_sum_two_pointers(arr, k):
    low = 0
    high = len(arr) - 1
    while high > low:
        total = arr[low] + arr[high]
        if total == k:
            return True
        elif total < k:
            low += 1
        else:
            high -= 1
    return False

print(pair_sum_two_pointers([1, 2, 3], 4))
print(pair_sum_two_pointers([1, 2], 4))
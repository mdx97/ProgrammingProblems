# Naive Solution.
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        soln = []

        for query_val in arr2:
            next_arr1 = []
            for val in arr1:
                if val == query_val:
                    soln.append(val)
                else:
                    next_arr1.append(val)
            arr1 = next_arr1
            
        arr1.sort()
        soln.extend(arr1)
        return soln

# Hash Table solution.
from collections import Counter

class Solution2(object):
    def relativeSortArray(self, arr1, arr2):
        counter = Counter(arr1)
        soln = []

        for num in arr2:
            soln.extend([num] * counter[num])
            del counter[num]
        
        for key in sorted(counter.keys()):
            soln.extend([key] * counter[key])

        return soln

sol = Solution2()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(sol.relativeSortArray(arr1, arr2))
# Naive Solution.
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        least_sum = -1
        
        for i, val1 in enumerate(list1):
            for j, val2 in enumerate(list2):
                index_sum = i + j
                if val1 == val2:
                    if (index_sum == least_sum or least_sum == -1):
                        least_sum = index_sum
                        ans.append(val1)
                    elif (index_sum < least_sum):
                        least_sum = index_sum
                        ans = [val1]
        
        return ans

# Dictionary Solution.
class Solution2:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurant_map = {}
        
        for i, val in enumerate(list1):
            restaurant_map[val] = [1, i]
        
        for i, val in enumerate(list2):
            if val in restaurant_map:
                restaurant_map[val] = [2, restaurant_map[val][1] + i]
            else:
                restaurant_map[val] = [1, i]
        
        least_index_sum = -1
        ans = []
        
        for key, val in restaurant_map.items():
            if val[0] != 2: continue
            if val[1] < least_index_sum or least_index_sum == -1:
                least_index_sum = val[1]
                ans = [key]
            elif val[1] == least_index_sum:
                ans.append(key)
        
        return ans

# Single Loop Solution
class Solution3:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_is = {val: i for i, val in enumerate(list1)}
        
        least_index_sum = -1
        ans = []
        
        for i, val in enumerate(list2):
            if val not in list1_is: continue
            index_sum = list1_is[val] + i
            if index_sum < least_index_sum or least_index_sum == -1:
                least_index_sum = index_sum
                ans = [cand]
            elif index_sum == least_index_sum:
                ans.append(cand)
        
        return ans
class Score:
    def __init__(self, num, idx):
        self.num = num
        self.idx = idx
        
class Solution:
    def findRelativeRanks(self, nums):
        size = len(nums)
        scores = [Score(num, idx) for idx, num in enumerate(nums)]
        scores.sort(key=lambda x: x.num, reverse=True)
        strings = ["" for x in range(size)]

        for i in range(size):
            score_index = scores[i].idx
            string = str(i + 1)
            if i == 0:
                string = "Gold Medal"
            elif i == 1:
                string = "Silver Medal"
            elif i == 2:
                string = "Bronze Medal"
            strings[score_index] = string
        
        return strings
        
sol = Solution()
print(sol.findRelativeRanks([5, 4, 3, 2, 1]))
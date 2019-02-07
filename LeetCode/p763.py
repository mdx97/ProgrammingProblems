class Solution(object):
    def partitionLabels(self, S):
        dictionary = {}

        for x in range(len(S)):
            c = S[x]
            dictionary[c] = x

        uniqueVals = []

        for x in range(len(dictionary)):
            val = dictionary.values()[x]
            if (val not in uniqueVals):
                uniqueVals.append(val)
        
        uniqueVals.sort()
        splits = []
        splitTotal = 0

        for uniqueVal in uniqueVals:
            splits.append(uniqueVal - splitTotal)
            splitTotal += uniqueVal
        
        return splits

sol = Solution()
print (sol.partitionLabels("ababcbacadefegdehijhklij"))
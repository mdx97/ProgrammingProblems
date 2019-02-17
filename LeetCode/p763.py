class Solution(object):
    def partitionLabels(self, S):
        dictionary = {}
        for x in range(len(S)):
            c = S[x]
            dictionary[c] = x

        unique_vals = []

        for x in range(len(dictionary)):
            val = dictionary.values()[x]
            if (val not in unique_vals):
                unique_vals.append(val)
        
        unique_vals.sort()
        splits = []
        split_total = 0

        for unique_val in unique_vals:
            splits.append(unique_val - split_total)
            split_total += unique_val
        
        return splits

sol = Solution()
print (sol.partitionLabels("ababcbacadefegdehijhklij"))
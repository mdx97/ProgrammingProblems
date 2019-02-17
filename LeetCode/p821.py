class Solution:
    def shortestToChar(self, S, C):
        indices = []
        for i in range(0, len(S)):
            if (S[i] == C):
                indices.append(i)
        
        distances = []

        for j in range(0, len(S)):
            smallest_sum = len(S)
            for char_index in indices:
                sum = abs(char_index - j)
                if (sum < smallest_sum):
                    smallest_sum = sum
            distances.append(smallest_sum)

        return distances
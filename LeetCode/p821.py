class Solution:
    def shortestToChar(self, S, C):
        indices = []
        for i in range(0, len(S)):
            if (S[i] == C):
                indices.append(i)
        
        distances = []

        for j in range(0, len(S)):
            small_total = len(S)
            for char_index in indices:
                total = abs(char_index - j)
                if (total < small_total):
                    small_total = total 
            distances.append(small_total)

        return distances

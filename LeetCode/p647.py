class Solution:
    def countSubstrings(self, s: 'str') -> 'int':
        size = len(s)
        dp = [[False for x in range(size)] for y in range(size)]
        for i in range(size):
            dp[i][i] = True
        count = size
        for length in range(2, size + 1):
            for start in range(size - length + 1):
                end = start + length - 1
                if start == end - 1:
                    dp[start][end] = (s[start] == s[end])
                else:
                    dp[start][end] = (s[start] == s[end]) and dp[start + 1][end - 1]
                
                if dp[start][end]:
                    count += 1

        return count

sol = Solution()
print(sol.countSubstrings("abc"))
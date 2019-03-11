class Solution(object):
    def coinChange(self, coins, amount):
        maximum = amount + 1
        dp = [maximum for x in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] < maximum else -1

sol = Solution()
print(sol.coinChange([1, 2, 5], 11))
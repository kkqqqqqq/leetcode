#
# @lc app=leetcode.cn id=518 lang=python3
# @lcpr version=30305
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp数组 含义 dp[i][j] 表示，用coins中的前i个coin，组成 j金额(amount=j)
        n = len(coins)
        dp = [ [0]*(amount+1) for _ in range(n+1)]
        for i in range(n + 1):
            dp[i][0] = 1
            
        
        for i in range(1,n+1):
            for j in range(amount+1):
                #没有第i个 coin的组合数 dp[i-1][j]
                #有第i个 coin的组合数， dp[i][j - coins[i - 1]]
                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][amount]

        
        
        
# @lc code=end



#
# @lcpr case=start
# 5\n[1,2,5]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[2]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[10]\n
# @lcpr case=end

#


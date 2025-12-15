#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30304
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 数组大小为 amount + 1，初始值也为 amount + 1
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin<0:
                    continue
                dp[i] = min (dp[i],dp[i-coin]+1)
        if dp[amount] == amount+1:
            return -1
        print(dp)
        return dp[amount] 
        
        
        
        
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#


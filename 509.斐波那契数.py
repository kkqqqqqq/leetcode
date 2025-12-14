#
# @lc app=leetcode.cn id=509 lang=python3
# @lcpr version=30304
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
       
        if n == 0 or n == 1:
            return n
        # dp table
        dp = [0] * (n + 1)
        # base case
        dp[0] = 0
        dp[1] = 1
        # 状态转移
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
        
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#


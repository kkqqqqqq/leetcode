#
# @lc app=leetcode.cn id=309 lang=python3
# @lcpr version=30305
#
# [309] 买卖股票的最佳时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp = [[0] * n for _ in range(2)]
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#


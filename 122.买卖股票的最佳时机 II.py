#
# @lc app=leetcode.cn id=122 lang=python3
# @lcpr version=30305
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for  i in range(1,len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp >0:
                ans += tmp
        return ans
# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#


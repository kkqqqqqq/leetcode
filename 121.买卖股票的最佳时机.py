#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30305
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i]:在第i天卖出能获得的最大利润
        dp = [0]*len(prices)
        # mmin:截止前一天的最小值
        mmin = 100000
        # mmax:最大利润
        mmax=0
        for i  in range(1,len(prices)):
            mmin = min(mmin,prices[i-1])
            dp[i]=prices[i]-mmin
            mmax = max(dp[i],mmax)
        return mmax
            
        
        
# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#


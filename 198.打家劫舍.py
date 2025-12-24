#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30305
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] 表示打劫到第i个房屋能够获取的最大金钱
        dp=[0]*(len(nums)+1)
        for i in range (1,len(nums)+1):
            dp[i] = max(dp[i-2]+nums[i-1],dp[i-1])
        return dp[len(nums)]
        
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#


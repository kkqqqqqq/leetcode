#
# @lc app=leetcode.cn id=213 lang=python3
# @lcpr version=30305
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 特判：只有一个房子
        if n == 1:
            return nums[0]
        # 两个及以上：分两种情况，去掉环形约束
        return max(self.rob1(nums[:-1]),self.rob1(nums[1:]))
    
    
    def rob1(self,nums: List[int])->int:
        dp=[0]*(len(nums)+1)
        dp[1] = max(dp[0],nums[0])
        for i in range (2,len(nums)+1):
            dp[i] = max(dp[i-2]+nums[i-1],dp[i-1])
        return dp[len(nums)]
        
# @lc code=end



#
# @lcpr case=start
# [2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30305
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 分割等和子集就是 分成两堆， 每一堆的和 = total_sum /2
        # 每个元素都是整数，因此，如果total_sum是奇数，total_sum/2为小数，必然不可能存在解
        total_sum = sum(nums)
        if total_sum%2 !=0:
            return False
        ssum = total_sum//2
        n=len(nums)
        # dp[i][j] 表示 使用nums中的前i个元素能不能凑出总和为j，true表示可以，false表示不可以
        
        dp =[[False]*(ssum+1) for _ in range(0,n)]
        
        for i in range(0,n):
            dp[i][0] = True
        
        for i in range(0,ssum+1):
            dp[0][i] = False
            
        dp[0][0]=True
        
        for i in range(1,n):
            for j in range(1,ssum+1):
                if  j-nums[i-1] <0:
                    dp[i][j] = dp[i-1][j]
                else:    
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
 
        return dp[n-1][ssum]
        
        
        
# @lc code=end



#
# @lcpr case=start
# [1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#


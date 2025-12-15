#
# @lc app=leetcode.cn id=931 lang=python3
# @lcpr version=30305
#
# [931] 下降路径最小和
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # 初始化dp数组
        # dp[i][j] 表示 从方形数组[i][j]为结尾的下降路径的最小和
        n = len(matrix[0])
        dp=[[0]*n for _ in range(n)]
        for i in range(0,n):
            dp[0][i] = matrix[0][i]
        
        for i in range(1,n):
            for j in range(0,n):
                if j ==0:
                    dp[i][j]= min(dp[i-1][j],dp[i-1][j+1])+matrix[i][j]
                elif j!= n-1:
                    dp[i][j]= min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])+matrix[i][j]
                else:
                    dp[i][j]= min(dp[i-1][j],dp[i-1][j-1])+matrix[i][j]
        ans = dp[n-1][0]
        
        print(dp)
        
        for i in range(1,n):
            ans = min (dp[n-1][i],ans)
        
        return ans
            
        
        



# @lc code=end



#
# @lcpr case=start
# [[2,1,3],[6,5,4],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[-19,57],[-40,-5]]\n
# @lcpr case=end

#


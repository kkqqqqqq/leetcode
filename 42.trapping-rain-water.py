#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left=[0]*len(height)
        right=[0]*len(height)
        i=1
        while i < len(height):
            left[i] = max(left[i-1],height[i-1])
            i +=1
        j=len(height)-2
        while j >=0:
            right[j]=max(right[j+1],height[j+1])
            j -=1
        ans = 0
        for index,h in enumerate(height):
            water_level = min(left[index], right[index])
            if water_level > h:
                ans += water_level - h
            
        return ans
            
        
                
        
        
# @lc code=end


#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i = 0
        j = 0
        ans = 0
        myset = set()
        while j<len(s):
            if s[j] not in myset:
                myset.add(s[j])
                ans = max(ans,j-i+1)
                j=j+1
            else:
                myset.remove(s[i])
                i += 1
        return ans            
        
        
        
# @lc code=end


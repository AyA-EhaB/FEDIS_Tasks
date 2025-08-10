class Solution(object):
    def lengthOfLongestSubstring(self, s):
       max_l =0
       left = 0
       unique = set()
       for right in range(len(s)):
           while s[right] in unique and left < len(s):
               unique.remove(s[left])
               left +=1
           unique.add(s[right])
           max_l = max(max_l ,right-left +1)

       return max_l

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))

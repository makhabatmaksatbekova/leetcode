# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3

class Solution:
    def lengthOfLongestSubstring(self, s):
        hash_map = {}
        lenghth=0
        result = 0
        for i in range(len(s)):
            if s[i] in hash_map and hash_map[s[i]]>=lenghth:
                lenghth=hash_map[s[i]]+1
            hash_map[s[i]]=i;
            result= max(result, i-lenghth+1)
        return result

s = "abcabcbb"

sol = Solution()
print(sol.lengthOfLongestSubstring(s))

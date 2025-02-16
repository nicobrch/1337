# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        A substring is a contiguous non-empty sequence of characters within a string.
        :type s: str
        :rtype: int
        """
        d = {}
        start = 0
        max_len = 0
        for i, c in enumerate(s):
            if c in d:
                start = max(start, d[c] + 1)
            d[c] = i
            max_len = max(max_len, i - start + 1)
        return max_len
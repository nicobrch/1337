class Solution(object):
    def longestPalindrome(self, s):
        """
        Finds the longest palindromic substring in s.
        :type s: str
        :rtype: str
        """
        longest_pal = ""
        longest_pal_len = 0

        for i in range(len(s)):
            # odd
            left_pivot, right_pivot = i, i
            while left_pivot >= 0 and right_pivot < len(s) and s[left_pivot] == s[right_pivot]:
                if (right_pivot - left_pivot + 1) > longest_pal_len:
                    longest_pal = s[left_pivot:right_pivot+1]
                    longest_pal_len = right_pivot - left_pivot + 1
                left_pivot -= 1
                right_pivot += 1

            # even
            left_pivot, right_pivot = i, i + 1
            while left_pivot >= 0 and right_pivot < len(s) and s[left_pivot] == s[right_pivot]:
                if (right_pivot - left_pivot + 1) > longest_pal_len:
                    longest_pal = s[left_pivot:right_pivot+1]
                    longest_pal_len = right_pivot - left_pivot + 1
                left_pivot -= 1
                right_pivot += 1

        return longest_pal

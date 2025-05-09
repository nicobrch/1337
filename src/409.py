from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1

        hashmap = defaultdict(int)
        res = 0

        for char in s:
            hashmap[char] += 1
            if hashmap[char] % 2 == 0:
                res += 2

        for count in hashmap.values():
            if count % 2:
                res += 1
                return res

        return res

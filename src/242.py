class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t and len(s) > 1 and len(t) > 1:
            return False

        hash_s = {}
        for char in s:
            hash_s[char] = 0

        for char in s:
            hash_s[char] += 1

        hash_t = {}

        for char in t:
            hash_t[char] = 0

        for char in t:
            hash_t[char] += 1

        if len(s) > len(t):
            for key, value in hash_s.items():
                if not hash_t.get(key):
                    return False
                elif hash_t.get(key) != value:
                    return False
        else:
            for key, value in hash_t.items():
                if not hash_s.get(key):
                    return False
                elif hash_s.get(key) != value:
                    return False

        return True

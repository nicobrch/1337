class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non alpha characters
        alpha = "".join(filter(str.isalnum, s))
        # pass to lowercase
        alpha = alpha.lower()
        rev = "".join(reversed(alpha))
        # check if is equal to reverse
        return True if alpha == rev else False

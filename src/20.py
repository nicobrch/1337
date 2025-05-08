from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False

        stack = deque()

        closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

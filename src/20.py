from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False

        stack_round = deque()
        stack_square = deque()
        stack_curly = deque()

        for char in s:
            if char == '(':
                stack_round.append(char)
            elif char == '[':
                stack_square.append(char)
            elif char == '{':
                stack_curly.append(char)

            if char == ')':
                if len(stack_round) > 0:
                    stack_round.pop()
                else:
                    return False

            if char == ']':
                if len(stack_square) > 0:
                    stack_square.pop()
                else:
                    return False

            if char == '}':
                if len(stack_curly) > 0:
                    stack_curly.pop()
                else:
                    return False

        return True

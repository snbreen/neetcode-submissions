from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parentheses = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in parentheses:
                if stack and stack[-1] == parentheses[char]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(char)

        return True if not stack else False

        
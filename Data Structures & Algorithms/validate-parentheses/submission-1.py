from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if stack: 
                    popped = stack.pop()
                else:
                    return False
                if char == ')':
                    if popped != '(':
                        return False
                elif char == '}':
                    if popped != '{':
                        return False
                else:
                    if popped != '[':
                        return False
        if stack: 
            return False
        
        return True

        
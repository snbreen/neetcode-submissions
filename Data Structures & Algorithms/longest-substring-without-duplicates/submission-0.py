class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        front = 0
        max_sub = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[front])
                front += 1
            chars.add(s[r])
            max_sub = max(max_sub, (r - front + 1))
        
        return max_sub


        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        front = 0
        back = len(s) - 1
        while back > front:
            if s[back] != s[front]:
                return False
            back -= 1
            front += 1
        return True
        
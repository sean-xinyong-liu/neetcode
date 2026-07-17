class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        length = len(s)
        left, right = 0, length - 1
        def is_alpha(c):
            if ('a' <= c and c <= 'z') or ('0' <= c and c <= '9'):
                return True
            return False
        while left < right:
            if not is_alpha(s[left]): 
                left += 1
            elif not is_alpha(s[right]):
                right -= 1 
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
            
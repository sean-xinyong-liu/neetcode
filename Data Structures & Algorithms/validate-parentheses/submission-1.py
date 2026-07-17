class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in mapping:
                if not stack:
                    return False
                if stack[-1] != mapping[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return False if stack else True




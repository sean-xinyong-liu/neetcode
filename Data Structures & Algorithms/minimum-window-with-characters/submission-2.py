from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(s), len(t)
        if n1 < n2:
            return ""

        left = 0
        valid = 0

        need = Counter(t)
        window = Counter()

        best_start = 0
        best_len = float("inf")

        for right, char in enumerate(s):

            if char in need:
                window[char] += 1
                if need[char] == window[char]:
                    valid += 1
            
            while valid == len(need):
                left_char = s[left]
                current_len = right - left + 1
                if current_len < best_len:
                    best_start = left
                    best_len = current_len

                if left_char in need:
                    if window[left_char] == need[left_char]:
                        valid -= 1
                    window[left_char] -= 1
                left += 1

        if best_len == float("inf"):
            return ""
                
        return s[best_start: best_start + best_len]




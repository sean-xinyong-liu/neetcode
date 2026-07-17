from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1: Counter[str] = Counter(s1)
        n1 = len(s1)
        n2 = len(s2)
        for i in range(n2 - n1 + 1):
            count2 = Counter(s2[i:i+n1])
            if count2 == count1:
                return True
        return False
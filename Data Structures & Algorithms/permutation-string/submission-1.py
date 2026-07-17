from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        count1 = Counter(s1)
        count2 = Counter(s2[: n1])
        if n1 > n2:
            return False
        for i in range(n2 - n1):
            if count2 == count1:
                return True
            count2[s2[i]] -= 1
            count2[s2[i + n1]] += 1
        return count2 == count1
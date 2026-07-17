class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + ":" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != ':':
                length += s[i]
                i += 1
            length = int(length)
            result.append(s[i + 1: i + 1 + length])
            i = i + 1 + length
        return result
            



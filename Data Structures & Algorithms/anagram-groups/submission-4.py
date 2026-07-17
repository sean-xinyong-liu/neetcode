class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))  # 将排序后的字符列表连接成字符串
            if s_sorted in str_map:
                str_map[s_sorted].append(s)
            else:
                str_map[s_sorted] = [s]
        return list(str_map.values())  # 直接返回字典的所有值

  
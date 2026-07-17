from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计频次
        count = Counter(nums)
        
        # 创建桶：索引表示频次，值是该频次的元素列表
        # 频次范围是 0 到 len(nums)，所以需要 len(nums) + 1 个桶
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # 将元素放入对应频次的桶中
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # 从高频到低频收集结果
        result = []
        for i in range(len(buckets) - 1, -1, -1):  # 从最大频次开始
            if buckets[i]:  # 如果桶不为空
                result.extend(buckets[i])  # 添加桶中的所有元素
                if len(result) >= k:  # 达到k个就停止
                    break
        
        return result[:k]  # 返回前k个元素





class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = total // 2

        left1, right1 = 0, n1 - 1

        while True:
            sep1 = (left1 + right1) // 2
            sep2 = half - sep1 - 2
            left_max1 = nums1[sep1] if sep1 >= 0 else float('-inf')
            left_max2 = nums2[sep2] if sep2 >= 0 else float('-inf')
            right_min1 = nums1[sep1 + 1] if sep1 + 1 < n1 else float('inf')
            right_min2 = nums2[sep2 + 1] if sep2 + 1 < n2 else float('inf')

            if left_max1 > right_min2:
                right1 = sep1 - 1
            elif left_max2 > right_min1:
                left1 = sep1 + 1
            else:
                if total % 2 == 1:
                    return min(right_min1, right_min2)
                else:
                    return (min(right_min1, right_min2) + max(left_max1, left_max2)) / 2
    


            

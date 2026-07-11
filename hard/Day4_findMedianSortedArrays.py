# 寻找两个正序数组的中位数
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n)) 。 


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): # 让nums1永远是短的那个数组
            nums1,nums2 = nums2,nums1
        m,n = len(nums1),len(nums2)
        left = 0
        right = m
        leftharf_len = (m + n + 1) // 2 # 将数据平分成左右两个篮子，希望的是左边篮子是较小的数，右边篮子是较大的数
        while left <= right :
            i = (left + right) // 2 # nums1切分位置，相当于nums1将i个数字放进左边篮子
            j = leftharf_len - i # nums2切分位置，相当于nums2将j个数字放进左边篮子，由于左边篮子总数是不变的，所以i多一个，j就少一个
            L1 = float('-inf') if i == 0 else nums1[i-1] # 注意边界
            R1 = float('inf') if i == m else nums1[i]
            L2 = float('-inf') if j == 0 else nums2[j-1]
            R2 = float('inf') if j == n else nums2[j]
            if L1 > R2:
                right = i - 1
            elif L2 > R1:
                left = i + 1
            else:
                max_left = max(L1,L2)
                if (m + n) % 2 == 1:
                    return float(max_left)
                min_right = min(R1,R2)
                return (max_left + min_right) / 2.0
            

        

# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
      
        新建一个长度为length的全0数组
        result = [0] * length

        for i in range (len(nums)):

            也可以用（i+k）% length来表示替换后的位置
            result[k - length + i] = nums[i]
          
        # 表示将nums数组替换成resul
        nums[:] = result       
        

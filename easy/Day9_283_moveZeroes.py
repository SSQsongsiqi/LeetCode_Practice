# 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。

# 先统计零的个数，删除零元素，后续统一在数组后面补0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                count += 1
                nums.remove(nums[i])
            else:
                i += 1
        for _ in range (count):
            nums.append(0)

# 双指针
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left] # 确保left左边都是吹好的元素，right寻找下一个即将处理的元素
                left += 1


        


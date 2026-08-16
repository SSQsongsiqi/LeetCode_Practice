class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hushtable = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in hushtable:
                return [hushtable[complement],i]
            hushtable[num] = i
        return []


# 注意 ： 在使用 enumerate 的时候，要先写下标，再写数值

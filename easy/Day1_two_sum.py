#解法一：暴力求解
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range (i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]

#解法二：哈希表求解（字典）
#重点是考虑到差值是否出现过
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hushtable={}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in hushtable:
                return [hushtable[complement],i]
            hushtable[num] = i
        return []

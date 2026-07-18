# 三数之和
'''
提示
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
'''

# 第一次运行，运行超时，只做记录
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        x = set()
        
        for i in range (len(nums)):
            y = set()
            for j in range (i+1,len(nums)):
                third = 0 - nums[i] - nums[j]
                if third in y:
                    triple = tuple(sorted([nums[i],nums[j],third])) # 集合里的元素必须是“不可变、可哈希”的对象。为了能放进集合，将列表转换成三元组
                    x.add(triple)
                y.add(nums[j])
        return [list(triple) for triple in x]
        
# 法一改进，可运行
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        x = set()
        nums.sort()
        for i in range (len(nums)):
            if nums[i] > 0: # 先将数组排序，如果第一个都>0，则直接退出
                break
            if i > 0 and nums[i] == nums[i-1]: # 不处理重复的数
                continue
            y = set()
            for j in range (i+1,len(nums)):
                third = 0 - nums[i] - nums[j]
                if third in y:
                    triple = tuple([nums[i],nums[j],third])
                    x.add(triple)
                y.add(nums[j])
        return [list(triple) for triple in x]
        
# 标准解法：双指针
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        x = []
        nums.sort()
        n = len(nums)
        for i in range (n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    x.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:  # 这里不用if用while的原因是：因为这里的目的不是判断一次有没有重复，而是把连续出现的所有重复值都跳过去。
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return x
            



        









            

            








            

            








            

            

# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。


# 考虑滑动窗口，但是滑动窗口并不适应于本题。因为数组可能有负数，并不是单增或单减
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        total = 0
        for right in range(len(nums)):
            count = count + nums[right]
            if count > k:
                count = count - nums[left]
                left += 1
            elif count == k:
                total += 1
                count = count - nums[left]
                left += 1
        return total

# 前缀和
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        current_sum = 0

        # 键：某个前缀和
        # 值：这个前缀和以前出现过几次
        sum_count = {0: 1}

        for num in nums:
            # 1. 计算当前位置的前缀和
            current_sum += num

            # 2. 想让某段子数组的和等于 k，
            #    前面就需要出现 current_sum - k
            target_sum = current_sum - k

            # 3. 如果这个前缀和以前出现过，
            #    出现几次，就代表找到了几个子数组
            if target_sum in sum_count:
                answer += sum_count[target_sum]

            # 4. 记录当前前缀和出现的次数
            if current_sum in sum_count:
                sum_count[current_sum] += 1
            else:
                sum_count[current_sum] = 1

        return answer

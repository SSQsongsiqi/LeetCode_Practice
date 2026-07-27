# 合并区间
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

# 先排序，后合并
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按照每个区间的左端点排序
        intervals.sort(key=lambda interval: interval[0])

        # 先把第一个区间放进结果列表
        result = [intervals[0]]

        # 从第二个区间开始遍历
        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]

            # result中最后一个已经合并好的区间
            last_end = result[-1][1]

            # 当前区间和上一个区间存在重叠
            if current_start <= last_end:
                result[-1][1] = max(last_end, current_end)

            # 当前区间和上一个区间没有重叠
            else:
                result.append(intervals[i])

        return result

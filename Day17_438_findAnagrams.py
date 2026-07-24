class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_count = Counter(p)
        window_count = Counter()

        left = 0

        for right in range(len(s)):
            # 把右指针当前字符加入窗口
            window_count[s[right]] += 1

            # 如果窗口长度超过 len(p)，删除最左边字符
            if right - left + 1 > len(p):
                window_count[s[left]] -= 1

                # 数量变成 0 后删除这个键
                if window_count[s[left]] == 0:
                    del window_count[s[left]]

                left += 1

            # 当两个字符统计完全相同时，说明是异位词
            if window_count == p_count:
                result.append(left)

        return result

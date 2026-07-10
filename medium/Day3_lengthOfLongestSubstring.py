#题目
#给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

#解答
#第一次暴力解答，出现错误，未考虑到重复的情况，例如：假设字符串是 "abcb"，当 i 指向 a，j 指向最后面的 b 时，s[i] != s[j] 确实成立（a != b），但其实中间已经包含重复的 b 了。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        len = len(s)
        i = 0
        j = i + 1
        for i,j in range(len):
            for s[i] != s[j]:
                j = j+1
                count = count + 1
            i = i + 1
        return count 


#使用集合正确解答
#优雅版，注意往集合里面加入和移除字符
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left = left + 1
            char_set.add(s[right])
            max_length = max(max_length,len(char_set))
        return max_length

#暴力求解，正确写法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for left in range(len(s)):
            char_set = set() # 【关键点】每次换新的起点，记忆(集合)必须清空重来
            for right in range(left, len(s)):
                if s[right] in char_set:
                    break # 【核心动作】立刻停止当前的内层探路，跳出循环，外层 left 就会自动 +1 进入下一轮
                char_set.add(s[right]) # 如果没重复，就记下来，并更新最大长度
                max_length = max(max_length, len(char_set))
        return max_length

# 编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != current_char:
                    return strs[0][:i]
        return strs[0]

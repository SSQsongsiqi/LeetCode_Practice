# 最长回文子串
# 给你一个字符串 s，找到 s 中最长的 回文 子串。

'''
示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
'''

'''
示例 2：
输入：s = "cbbd"
输出："bb
'''

# 暴力求解
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_pal = ""
        for left in range(len(s)):
            for right in range (left,len(s)):
                if s[left] == s[right]:
                    pal = s[left : right+1] #切片
                    if pal == pal[: : -1]:  # 检查这段嫌疑子串是不是真正的回文
                        if len(max_pal) < len(pal):
                            max_pal = pal
        return max_pal

# 考虑对称
# 视角翻转，随便定一个字母，向其两边扩散，左边=右边，即是回文（对称性）
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        max_len = 0

        # 定义一个扩散函数
        def expand_around_center(left:int,right:int)->int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range (len(s)):
            len1 = expand_around_center(i,i) # 长度为奇数时
            len2 = expand_around_center(i,i+1) # 长度为偶数时
            current_max_len = max(len1,len2)
            if current_max_len > max_len:
                max_len = current_max_len
                start = i - (max_len-1)//2 # 当长度为偶数时，start=i-(l/2-1) ; 当长度为奇数时，start=i-(l-1)/2
        return s[start : start+max_len]




            




            

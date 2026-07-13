# "Z"字变换
# 这道题第一次写不太会，后续多练
'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：
输入：s = "A", numRows = 1
输出："A"
'''

# 暴力枚举
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        row = []
        T = 2*numRows - 2
        for j in range (numRows):
            for i in range (len(s)):
                if (i - j) % T == 0 or (i + j) % T == 0:
                    row.append(s[i])
        return "".join(row)

# 模拟法
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 只有一行时，不需要进行 Z 字形转换
        if numRows == 1 or numRows >= len(s):
            return s

        # 每个列表存放一行的字符
        rows = [[] for _ in range(numRows)]

        current_row = 0 # 表示当前行
        direction = 1  # 1 表示向下，-1 表示向上

        for char in s:
            rows[current_row].append(char)

            # 到达第一行，接下来向下走
            if current_row == 0:
                direction = 1

            # 到达最后一行，接下来向上走
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        # 先拼接每一行，再把所有行拼接起来
        return "".join("".join(row) for row in rows)


                    

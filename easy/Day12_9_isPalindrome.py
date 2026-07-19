# 法一，直接反转
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False

# 法二，不用字符串
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reversed_num = 0
        while x > 0:
            digit  = x % 10                               # 取出最后一位
            reversed_num = reversed_num * 10 + digit      # 将取出来的原右侧数放入反转数的左侧数，为了后面判断是否反转后与原数一致
            x //= 10                                      # 丢掉最后一位，继而只用判断前面的数

        return original == reversed_num

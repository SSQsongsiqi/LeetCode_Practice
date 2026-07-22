# 有效的括号

class Solution:
    def isValid(self, s: str) -> bool:
        char = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                char.append(s[i])
            elif s[i] == ')':
                if char and char[-1] == '(':
                    char.pop()
                else:
                    return False
            elif s[i] == ']':
                if char and char[-1] == '[':
                    char.pop()
                else:
                    return False
            elif s[i] == '}':
                if char and char[-1] == '{':
                    char.pop()
                else:
                    return False
            if i == len(s) - 1 and len(char) != 0:
                return False
        return True

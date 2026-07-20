class Solution:
    def romanToInt(self, s: str) -> int:
        hushtable = {}
        hushtable['I'] = 1
        hushtable['V'] = 5
        hushtable['X'] = 10
        hushtable['L'] = 50
        hushtable['C'] = 100
        hushtable['D'] = 500
        hushtable['M'] = 1000

        i = 0
        result = 0
        while i < len(s):
            if i+1 < len(s) and hushtable[s[i]] < hushtable[s[i+1]]:
                result += hushtable[s[i+1]] - hushtable[s[i]]
                i += 2
            else:
                result += hushtable[s[i]]
                i += 1
        return result

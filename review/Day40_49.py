class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            char = "".join(sorted(word))
            if char not in group:
                group[char] = []
            group[char].append(word)
        return list(group.values())




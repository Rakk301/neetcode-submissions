class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            check = strs[0][i]
            for s in strs: 
                if len(s) == i or s[i] != check:
                    return strs[0][:i]
        return strs[0]
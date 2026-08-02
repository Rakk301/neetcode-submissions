class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = min(strs, key=len)
        if len(mini)<1:
            return ""
        for i in range(len(mini)):
            temp = mini[:i+1]
            for s in strs:
                if temp in s[:i+1]:
                    continue 
                else: 
                    return temp[:-1]
        return temp
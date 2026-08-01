class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        if len(s) <1:
            return True
        while i < len(t):
            if s[j] == t[i]:
                j+=1
                if j == len(s):
                    return True
            i+=1
        return False

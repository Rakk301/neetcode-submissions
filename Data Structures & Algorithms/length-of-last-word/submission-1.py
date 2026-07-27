class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        cnt =0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                return cnt
            cnt+=1   
        return cnt     
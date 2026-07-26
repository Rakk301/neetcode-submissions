class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_count=0
        s_count=0
        if len(s) ==0:
            return True
        while t_count < len(t): 

            if t[t_count] == s[s_count]: 
                s_count +=1
                t_count +=1
            else: 
                t_count +=1
            if s_count == len(s):
                return True 
        return False



        
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t={}
        t_s={}
        for i in range(len(s)):
            if s[i] not in s_t.keys() and t[i] not in t_s.keys(): 
                s_t[s[i]] = t[i]
                t_s[t[i]] = s[i]
            else: 
                if s_t.get(s[i],0) == t[i] and t_s[t[i]] == s[i]:
                    continue
                else: 
                    return False 
        return True 


# a-a ; a-a
# b-b ; b-b

        
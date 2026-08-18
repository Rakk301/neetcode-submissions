class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().replace(' ','') 
        for c in s :
            if c.isalnum():
                continue
            else:
                s=s.replace(c,'')
        i=0
        j=len(s)-1
        for i in range(0, len(s)//2):
            if s[i] == s[j]:
                j-=1
                continue 
            else:
                return False 
        return True
        
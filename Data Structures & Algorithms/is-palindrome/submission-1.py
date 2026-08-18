class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join([c for c in s.lower() if c.isalnum()])
        i=0
        j=len(s)-1
        for i in range(0, len(s)//2):
            if s[i] == s[j]:
                j-=1
                continue 
            else:
                return False 
        return True
        
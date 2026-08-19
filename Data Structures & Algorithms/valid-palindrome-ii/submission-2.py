class Solution:
    def validPalindrome(self, s: str) -> bool:
        error=1
        s=''.join([c for c in s.lower() if c.isalnum()])
        l = len(s)
        j=l-1

        def is_pal(i,j):
            while i<j:
                if s[i] != s[j]:
                    return False
                j-=1
                i+=1
            return True
        
        p=l-1
        for i in range(l//2):
            if s[i] != s[p]:
                return is_pal(i+1, p) or is_pal(i, p-1)
            p-=1
        return True
        
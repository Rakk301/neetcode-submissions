class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        tmp1 = ''
        tmp2 = ''

        for i in range (0,len(s)//2):
            tmp1 = s[i]
            tmp2 = s[j]
            s[i] = tmp2
            s[j] = tmp1
            j-=1
        


        
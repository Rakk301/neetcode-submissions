class Solution:
    def maxDifference(self, s: str) -> int:
        cnts = {}
        for char in s:
            cnts[char] = cnts.get(char,0)+1
        evens=set()
        odds=set()
        minimum=100
        maximum=0
        for k,v in cnts.items():
            if v%2==0: 
                if v<minimum :
                    minimum=v
            else:
                if v>maximum : 
                    maximum =v
        return maximum-minimum


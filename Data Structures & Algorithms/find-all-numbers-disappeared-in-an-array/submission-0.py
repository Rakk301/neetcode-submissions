class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        disap =[]

        for i in range(1,n+1):
            if i not in nums:
                disap.append(i)
        
        return disap

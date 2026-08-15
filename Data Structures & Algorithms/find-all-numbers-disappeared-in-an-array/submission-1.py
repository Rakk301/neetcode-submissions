class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        disap =[]
        seen = set()

        for nu in nums:
            seen.add(nu)

        for i in range(1,n+1):
            if i not in seen:
                disap.append(i)        
        return disap

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


        nu = [0] + nums + [0]

        for i in range(1,len(nu)-1):
            if sum(nu[:i]) == sum(nu[i+1:]):
                return i-1
        return -1
        
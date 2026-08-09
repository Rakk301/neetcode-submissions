class Solution:
    def majorityElement(self, nums: List[int]) -> int:   
        currents = nums[0]
        cnts = 0

        for n in nums :
            if n == currents :
                cnts+=1
            else :
                cnts-=1
            if cnts == 0:
                currents = n
                cnts=1
        return currents
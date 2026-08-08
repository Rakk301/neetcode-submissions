class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = nums[0]
        cnt = 0
        for n in nums :
            if n == current :
                cnt+=1
            else:
                cnt-=1
            if cnt==0:
                current = n
                cnt =1
        return current

        
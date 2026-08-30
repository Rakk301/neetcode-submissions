class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        curr = -101
        for i in range(len(nums)):
            if nums[i] != curr:
                nums[write] = nums[i]
                write+=1
                curr=nums[i]
        return write
            

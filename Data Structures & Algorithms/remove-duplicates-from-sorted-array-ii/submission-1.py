class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        curr_num = nums[0]
        seen = 0
        for i in range(len(nums)):
            if nums[i] == curr_num:
                seen += 1
            elif nums[i] != curr_num:
                curr_num = nums[i]
                seen = 1
            nums[w] = nums[i]
            if seen <= 2: 
                w+=1
        
        return w



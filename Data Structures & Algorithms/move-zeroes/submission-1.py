class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,nz = 0,0

        for i in range(len(nums)):
            if nums[i] !=0 and i==nz :
                nz+=1
            elif nums[i] !=0:
                nums[nz] = nums[i]
                nums[i] = 0
                nz+=1
            


        
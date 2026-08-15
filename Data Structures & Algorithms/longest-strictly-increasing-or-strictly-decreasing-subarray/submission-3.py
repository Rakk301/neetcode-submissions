class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        last = nums[0]
        dec = 1
        inc = 1 
        max_dec = 0
        max_inc = 0

        for i in range(1,len(nums)):
            if nums[i]>last:
                inc+=1
                dec=1
            elif nums[i]<last:
                dec+=1
                inc=1
            else :
                dec =1
                inc =1
            if dec > max_dec:
                max_dec = dec
            if inc > max_inc:
                max_inc  = inc
            last = nums[i]
        return max(max_inc,max_dec,1)


        
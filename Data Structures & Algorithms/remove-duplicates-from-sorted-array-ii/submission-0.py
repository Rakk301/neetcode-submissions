class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        digits = {}
        i=0
        for n in nums:
            digits[n] = digits.get(n,0) +1
        
        for num in digits.keys():
            for l in range(min(digits[num],2)):
                nums[i] = num
                i+=1
        return i
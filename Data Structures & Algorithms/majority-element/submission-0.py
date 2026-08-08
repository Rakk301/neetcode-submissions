class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         nums_s = nums.sort()
         return nums[len(nums)//2]

        
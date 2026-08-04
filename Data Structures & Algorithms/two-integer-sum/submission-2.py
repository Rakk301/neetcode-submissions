class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen: 
                return[seen[diff], i]
            seen[nums[i]] = i
    
# #1: 
# i =0; nums[i]=4; diff=6
# seen{4:0}
# in NO 

# #2
# i=1; nums[i]=5; diff=5
# seen{5:1}
# in YES 
# return[]
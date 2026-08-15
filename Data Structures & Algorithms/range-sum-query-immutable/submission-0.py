class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.running_total =[0]
        running=0

        for n in self.nums: 
            running+=n
            self.running_total.append(running)

    def sumRange(self, left: int, right: int) -> int:
        return (self.running_total[right+1]-self.running_total[left])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
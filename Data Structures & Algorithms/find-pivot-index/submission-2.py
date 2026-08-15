class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


        nu = [0] + nums + [0]
        total = sum(nu)
        running_total = 0

        for i in range(1,len(nu)-1):
            running_total += nu[i-1]
            total-= nu[i]
            if running_total == total:
                return i-1
        return -1
        
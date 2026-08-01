class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        run_cnt = 0
        cnt_max =0
        for i in nums: 
            if i == 1: 
                run_cnt += 1
                if run_cnt > cnt_max: 
                    cnt_max = run_cnt 
            else :
                run_cnt = 0
        return cnt_max
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = {}

        for s in arr:
            cnt[s] = cnt.get(s,0) +1
        
        cnt_unique = {k: v for k,v in cnt.items() if v == 1}
        if k-1>= len(cnt_unique):
            return ""
        else:
            ind = list(cnt_unique.keys())[k-1]
            return ind
        
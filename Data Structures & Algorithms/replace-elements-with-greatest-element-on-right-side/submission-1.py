class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lookup = -1
        tmp=arr.copy()
        for i in range (len(arr)-1, -1, -1): 
            if arr[i] > lookup: 
                lookup = arr[i]
            tmp[i-1] = lookup 
        tmp[-1] = -1
        return tmp


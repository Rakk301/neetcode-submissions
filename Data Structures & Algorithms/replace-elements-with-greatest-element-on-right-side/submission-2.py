class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lookup = -1
        for i in range (len(arr)-1, -1, -1): 
            tmp = arr[i]
            arr[i] = lookup
            lookup = max(lookup, tmp)
        return arr   


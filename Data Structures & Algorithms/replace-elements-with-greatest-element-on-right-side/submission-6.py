class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lookup = -1
        tmp = 0
        i=len(arr)-1
        while i !=-1:
            tmp = arr[i]
            arr[i] = lookup
            if lookup < tmp:
                lookup = tmp 
            i-=1
        return arr
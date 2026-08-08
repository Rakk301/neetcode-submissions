class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zero_count = 1
        i=0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                zero_count+=1
            else:
                zero_count =0 
            if zero_count >1 and zero_count%2==1:
                n-=1
            if n ==0:
                return True 
            i+=1 
        if zero_count ==2:
            n-=1
        if n==0:
            return True 
        else: 
            return False 
        
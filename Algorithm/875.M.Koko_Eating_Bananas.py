class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #용량 / 시간 안에 문제 나오면 binary search
        #nlogm 
        #485ms 93.33% faster / 15.4 less than 74.79%
        def isAvailable(k):
            hours = 0
            i=0
            for p in piles : 
                hours+=math.ceil(p /k)
            if hours<=h : return True
            else : return False
        
        
        l, r = 1,max(piles)
        while l<r : 
            mid = (l+r)//2
            if isAvailable(mid) : 
                r = mid
            else : 
                l = mid+1
        return r
        
            
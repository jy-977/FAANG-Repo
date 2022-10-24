class Solution:
    def search(self, nums: List[int], target: int) -> int:
#        prob analy
#       1) small range
#       2) sorted array
#       3) O(log n) --> binary search
        #81ms 50.03% faster / 14.3mb 55.62% less
        l,r = 0, len(nums)-1
        while l<=r: 
            mid = l + (r-l)//2
            l_reverse = True if nums[l] >nums[mid] else False
            if nums[mid]== target : 
                return mid
            elif not l_reverse : 
                if target>=nums[l] and target<nums[mid] : 
                    r = mid-1
                else : 
                     l = mid+1 
            else : 
                if target<=nums[r] and target>nums[mid]: 
                    l = mid+1
                else : 
                    r = mid-1
        return -1
    #원리는 이해를 했는데,, 
    #mid = l+(r-l)//2 이거랑 
    #인덱스 조절이 너무 어려움,,, 
    #2번 풀었는데 두번 다 영 시원찮다
    
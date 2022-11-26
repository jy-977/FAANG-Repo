from collections import deque
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        nums = deque(nums)
        nums.appendleft(lower-1)
        nums.append(upper+1)
        for i in range(1,len(nums)) : 
            if nums[i]-nums[i-1]>1 :
                if nums[i-1]+1 == nums[i]-1 : 
                    res.append(str(nums[i-1]+1))
                else : 
                    res.append(str(nums[i-1]+1)+"->"+str(nums[i]-1))
        return res



58 ms, 40.18 faster
14 MB, less than 35.44% 
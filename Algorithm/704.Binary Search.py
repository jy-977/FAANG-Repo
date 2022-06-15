import random
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i,n in enumerate(nums):
            if(n == target): return i
            elif(n>target): return -1
        return -1
        
        
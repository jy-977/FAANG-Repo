class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        mark = 0
        for i in range(len(nums)) : 
            if nums[i] != val : 
                nums[mark] = nums[i]
                mark+=1
        return mark
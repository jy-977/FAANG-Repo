class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # problem analysis
        # 1) range big : hash bitmask binarysearch twopointers slidingwindow
        # 2) in place : space complexity - O(1)
        
        
        #idea 1 ) two pointers   : 182 ms (88.01 faster) 15.6mb (66.26 less)
        left , right =0,1
        while ( left< right) :
            if (right> len(nums)-1):
                return
            if(nums[left]==0 and nums[right]!=0) :
                nums[left], nums[right]  = nums[right], nums[left]
            if (nums[left]!=0) : 
                left +=1
            right +=1
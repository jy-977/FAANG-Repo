class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # problem analysis
        # 1) two pointers
        # 2) space complexity O(1)
        # 3) time complexity O(n)

        # idea 1) two pointers
        # summary ) swap ends till reaching middle
        
        left , right = 0, len(s)-1
        while(left<right):
            s[left],s[right]=s[right],s[left]
            left=left+1
            right=right-1
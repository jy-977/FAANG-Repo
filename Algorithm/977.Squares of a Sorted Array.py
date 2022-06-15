class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
# 문제분석
# 1) Sorting
# 2) O(n)


# idea 1) using python included methods
#  파이썬 sorted complexity O(nlogn)
        return(sorted(list(map(lambda x : x*x,nums))))

# idea 2) 
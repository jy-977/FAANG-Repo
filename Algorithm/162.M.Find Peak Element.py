class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #problem analysis
        #1) range : small
        #2) O(logn ) ==> binary search
        #search 
        #not sorted...
        
        #You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array. 
        #이게 무슨 힌트인지 감을 못잡겠다
        #
        
#idea 1 : binary search

#HOW TO BINARY SEARCH WITH UNSORTED ARRAY?
#1) SORT // HASHMAP?
#2) BS
#성능이 심히 걱정된다 ㅋㅋ,,
        
# ==================================================================    
    
#  solution 봄 !!!  (92ms 16.2% faster / 14mb 82.73% less)
#1) binary search : 맞음
#2) unsorted array binary search?
#힌트 1) nums[-1] = nums[n] = -∞.  : 시작과 끝이 상승ㅇ로 시작함
#힌트 2) nums[i] != nums[i + 1]
            left , right = 0, len(nums)-1
            while(left<right) :
                mid = int((left+right)/2)
                if(nums[mid]<nums[mid+1]) : 
                    left = mid+1
                else : 
                    right = mid
            return left





# ------------------------------------------------------------------
#회고!
#1) 문제이해 부족
    #나는 max값의 idx 를 뽑아 내는거라고 생각했는데 피크의 idx중 아무거나 리턴하면됨
#2) 힌트 이해부족
    #nums[-1] = nums[n] = -∞.  의 의미와 nums[i] != nums[i + 1]가 가져오는 상승 / 하강의 개념이해 부족

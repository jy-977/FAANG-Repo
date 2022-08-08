class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#     PROBLEM ANALYSIS
#        - BIG RANGE : BITMASK, SET.. 

# IDEA 1 )  set  195ms 171.mb
#  ADD COMPONENTS TO SET 
#  4 --> 4,1 --> 4,1,2 ==> 4,1,2,1 
# IF NEW COM IN SET : DROP COM  ( 4,2)
# AFTER LOOP : RETURN FINAL SET
        # s = set()
        # for i in range(len(nums)) :
        #     if(nums[i] in s ) : 
        #         s.remove(nums[i])
        #     elif ( nums[i] not in s) : 
        #         s.add(nums[i])
        # return list(s)[0]

# IDEA 2) BIT MASKING : 234ms (42.66% faster) 16.9mb (20%.31 less)
# xor : 같으면 0 다르면 1
# 일단 쓰면 비트마스킹은 규칙찾기가 수월하다!
        xor = nums[0]
        for i in range(1,len(nums)): 
            xor = (xor ^ nums[i])
            
        return xor
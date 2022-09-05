class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #problem analysis 


        #처음에 set도 생각했는데 .. 마무리 못하고 넘어갔음


        #idea 1) hashmap 452ms 98.35%  / 25.9mb 90.60 % 
        hashmap = {}
        for i in range(len(nums)) :  
            if (nums[i] in hashmap) : 
                return True
            else : 
                hashmap[nums[i]] = 1

        #solution 2 ) 825ms 24.78% faster / 26.2 mb 28.71 less
        return True if len(set(nums))<len(nums) else False

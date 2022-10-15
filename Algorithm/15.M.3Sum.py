class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #neetcode 참고 : 809ms 9.12% faster  18.2 less than 39.99%
        nums.sort()
        output =[]
        for i,a in enumerate(nums[:-2]) :
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i+1, len(nums)-1

            while l<r:
                tsum = a+nums[l]+nums[r]
                if tsum<0 : 
                    l+=1
                elif tsum>0 : 
                    r-=1
                if tsum==0 : 
                    output.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r : 
                        l+=1
        return output
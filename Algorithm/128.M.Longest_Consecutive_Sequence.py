class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #10^5 :
        #10^9 : O(n)

        #O(n) : hashmap, bit manipulation, two pointers, sliding window, set
        
        #idea1 : bruteforce 10^9
        67/72

        # max_longest = 0
        # longest = 0
        # if len(nums)>0 : 
        #     minn, maxx= min(nums), max(nums)
        #     for i in range(minn,maxx+1) :
        #         if i in nums : 
        #             longest +=1
        #             max_longest = max(max_longest, longest)
        #         else : 
        #             longest = 0
        #     return max_longest
        # else : return 0
        
        #idea 2 : union-find
        #기본 union find가 아님
        
        #1. parent init
        # parent = {}

        # longest = 0
        # #2. def union

        # def union(x,y) :
        #     a = find(x)
        #     b = find(y)
        #     if a and b : 
        #         if(a<b) : parent[b] = a
        #         else : parent[a] = b
        # #3. def find
        # def find(x) : 
        #     depth+=1
        #     if x not in parent : 
        #         return False
        #     if parent[x] == x : return x
        #     else : 
        #         parent[x] = find(parent[x])
        #         return parent[x]
        
        # #4. compare
        # for i in nums : 
        #     if i in parent : 
        #         continue
        #     if i-1 in parent : 
        #         union(i,i-1)
        #     if i+1 in parent : 
        #         union(i,i+1)
        # for p in parent : 
        #     if p!=parent[p] :
        #         find(p)
        
        # return 0
        
        #idea 3 :Set 2127ms 36.35% faster / 29mb 63.36% less
        numset = set(nums)
        longest = 0
        for n in nums : 
            if n-1 not in numset :
                leng = 1
                while n+leng in numset : 
                    leng +=1
                longest = max(longest, leng)
            
        return longest
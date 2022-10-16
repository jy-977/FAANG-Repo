class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         598ms 99.62% faster / 32.2mb 13.84% less
        hm = {}
        for n in nums :
            if hm.get(n,0) : 
                return n
            else : 
                hm[n] = 1

# floyd로 푸는 다른 방법이 있는데 이건 hard에 적합한 문제임

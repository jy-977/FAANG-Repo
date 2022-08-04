class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
#     dp 판별 조건
# 1. 작은 부분으로 쪼갠다
# 2. 반복

# 아직 이걸 기준으로 dp 인걸 생각해낼 눈이 없다..

# 문제를 쪼개서 생각하는 힘이 있어야함!
# 1,2,3,4 까지 생각하면 보통 재귀관계가 나와야하는데

# ----------------------------------------------------------------------------------
# idea 1) dp
# dq점화식 : f(x) 배열이 길이가 x일때의 array 의 합
# odd) f(x) = max(f(floor[x/2]), f(ceil[x/2])) 
# even) f(x) = max(f[x/2])


# ----------------------------------------------------------------------------------
# IDEA 2:
# IDEA1의 재귀식이 잘못된게 X의 의미가 다름
# 이런문제는 앞에서 부터 하나씩 봐야하니까 X : INDEX임

# idx = x일때 x를 터느냐 안터느냐
# f(x) = max(f(x-1), f(x-2) + nums[x]) ---> 점화식


# 구현방법 4가지
#  recursion ( topdown)
#  recursion + memo (topdown)
#  iteration + memo (bottom up) ==> 내가 좋아하는 방식!
#  iteration + 2 variables (bottom up)


# 1)iteration + memo : 48ms , 13.9mb
        n = len(nums)
        memo = [0 for _ in range(n)]
        memo[0] = nums[0]
        if(n>1) : 
            memo[1] = max(memo[0], nums[1])  
            for x in range(2, n) :
                    memo[x] = max(memo[x-1] , memo[x-2]+nums[x])
        return memo[n-1]    
            
        





# ----------------------------------------------------------------------------------
# FORUM IDEA 
# 대부분의 문제를 푸는 방법
# 1) 재귀관계 (점화식)파악
# 2) 구현
#     2-1) RECURSSION (TOP DOWN)
#     2-2) RECURSSION + MEMO (TOP DOWN)
#     2-3) ITERATION + MEMO (BUTTOM UP)
#     2-4) ITERATION + 2 VARIABLES ( BUTTOM UP) ==> MEMO 대신 F(N-1) , F(N-2)의 값만 기억

# 사실 제일 중요한거는 재귀관계 파악인디.. 이게 어렵다

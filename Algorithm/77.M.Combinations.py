from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

# idea 1) python build in function : 89ms, 15.9mb
        input = [x for x in range(1,n+1)]
        return list(combinations(input,k))

#     checkpoint 1) 배열 선언시 comprehension으로하기
#     checkpoint 2) combinations, permutations import 사용법!


# idea 2) iterative ==> no .. 
    # O(n) = n*(n-1)*(n-2) ... = 2*n    
        

# idea 3) recursive.. & backtracking? : 97ms , 15.9Mb
#         backtrancking : dfs 를 포함하는 개념...? - prunning : 가지치기
#         dfs 구현시 recursive 로 구현함.. 


        output = []
        s = set()
        def dfs():
#           1) return condition
            if len(s) == k : 
                output.append(list(s))
                return
            
            
#           2) main action : put number on set S
            for num in range(1,n+1) :
                if(num not in s) : 
                    s.append(num)
                    dfs()
                    s.remove(s)
        dfs();
        return s

# content 
# 아직 dfs 공식 못 외운듯

# 1)return condition
# 2) main action
# 3) call recursive 
# 백준 N과 M 풀이 많이 참고함.. 733 dfs문제풀이도 참고함!
# 괜찮아! 담엔 안보고 하면되지!

from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
# idea 1 : python built in function : 62ms , 13.7mb
        # return permutations(nums, len(nums))

# idea 2: Backtracking DFS (recursive) : 49ms , 14.1mb
       
        output=[]
        stack = list()
        def dfs () : 
            # 1) return conditions
            if(len(stack)==length):
                output.append(list(stack))
                return 
            
            # 2) main action : put number on List "stack"            
            for num in nums : 
                if(num not in stack) : 
                    stack.append(num)
                    dfs()
                    stack.pop()
                    
                    
        length = len(nums)
        dfs()
        return output
                    
            
            
# dfs 공식
# 1) return conditon
# 2) main action
# 3) call recursively


# content 
    # output.append(list(stack)) vs output.append(stack)
    # 여기서 list(stack) 아니고 stack()으로만 append하면 결과물이 [[],[],[],[]] 이 나옴.. 왜그런거지..
    # 배열과 list의 차이같은데 배열은 주소로 다루고 list는 값으로 나오는건가 0
    # 배열은 값이 아니라 주소를 가리킴..

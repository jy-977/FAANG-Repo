class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
# problem anaysis
# 1) sorted array
# 2) search


# IDEA 1) binary search (82ms 27.17% faster / 14.4mb 89.21% less)
        m, n = len(matrix),len(matrix[0])
        left, right = 0, m*n-1
        # print(int(right/n),
        
        while left<=right : 
            mid = int((left+right)/2)
            r =  int(mid/n)
            c = mid-r*n
            if(matrix[r][c]== target) : return True
            elif ( matrix[r][c]< target) : left = mid +1
            else : right = mid-1
        return False
    
    
# IDEA 2) build in : (53MS 80% FASTER / 14.4MB 89.21 LESS)
        # for _ in matrix : 
        #     if target in _ : return True
        # return False
        
# IDEA 3) BRUTE FORCE
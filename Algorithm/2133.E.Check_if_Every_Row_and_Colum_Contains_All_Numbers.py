class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        #object : 
            # row, col : 1-n?

        #analysis : 
            # O(n) : n^2
            #Array / Hashmap

        #idea 1 : BruteForce Runtime
        # 1053 ms 72.77% 
        # 14.4 MB 87.55%
        # n = len(matrix)
        # row = {i+1 : [] for i in range(n)}  # key : val => num : idx array 
        # col = {i+1 : [] for i in range(n)}  # key : val => num : idx array
        # for i in range(n) : 
        #     for j in range(n) : 
        #         val = matrix[i][j]
        #         #row check
        #         if i in row[val] : 
        #             return False
        #         else : 
        #             row[val].append(i)
        #         #col check
        #         if j in col[val]: 
        #             return False
        #         else : 
        #             col[val].append(j)

        # return True

        #idea 2: 
        
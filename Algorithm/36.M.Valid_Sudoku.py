class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #requirement
        # sudocku valid?

        #analysis   
        
        #CHEKER : ROW, COL, BOX


        #IDEA 1) BRUTEFORCE : 100ms beats 89,43 faster / 13.9mb 35.31% ess
        row = {str(i+1) : [] for i in range(9)} #key: value == row : num
        col = {str(i+1) : [] for i in range(9)} #key : value== col : num
        box = {str(i+1) : [] for i in range(9)} #key : value == box : num
        
        def rowCheck(r, val) :
            if r in row[val]: 
                print("here row!",  r, val, row)
                return False
            else : 
                row[val].append(r)
                return True

        def colCheck(c, val): 
            if c in col[val] : 
                print("here col!", c, val)
                return False
            else : 
                col[val].append(c)
                return True

        def boxCheck(r,c, val) : 
            #which boxk : 
            boxx = r//3*3+ c//3
            if boxx in box[val] : 
                print("here box!", boxx, val)
                return False
            else: 
                box[val].append(boxx)
                return True



        for i in range(9) : 
            for j in range(9) :
                val =board[i][j]
                if val.isdigit() :  
                    #rowcheck
                    if not rowCheck(i,val): 
                        return False
                    #colcheck
                    if not colCheck(j,val): 
                        return False
                    #boxcheck
                    if not boxCheck(i,j,val): 
                        return False
        return True
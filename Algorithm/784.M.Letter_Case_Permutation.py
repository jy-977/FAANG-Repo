class Solution:
    # def letterCasePermutation(self, s: str) -> List[str]:
    #     #tree 구조
    #     #bfs?
    #     res = []
    #     i,cur =0,''
    #     def recurse(i,cur) : 
    #         #break point
    #         if i == len(s) : 
    #             res.append(cur)
    #             return 
            
    #         if s[i].isalpha() :
    #             options = [s[i].upper(), s[i].lower()]
    #             for option in options : 
    #                 recurse(i+1, cur+option)
    #         else : 
    #             recurse(i+1, cur+s[i])
    #     recurse(i,cur)
    #     return res

        def letterCasePermutation(self, S):
            res = ['']
            for ch in S:
                if ch.isalpha():
                    res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
                else:
                    res = [i+ch for i in res]
            return res

        #이중 list comprehension
#back tracking
#38 94.79% faster  5.86% less


class Solution:
    def expand(self, s: str ) -> List[str]:
        res = []
        i=0
        cur =''
        
        def recursive(i,cur) :
            if i==len(s) : 
                res.append(''.join(cur))
                return             
            if s[i] == '{': 
                i+=1
                end = s.index("}", i)
                options = s[i:end].split(',')
                for option in options : 
                    recursive(end+1, cur+option)
            else : 
                recursive(i+1,cur+s[i])

        recursive(i,cur)
        return sorted(res)
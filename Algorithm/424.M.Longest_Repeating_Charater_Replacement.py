#435ms 18.37% faster /14mb 57.07 faster
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char ={}
        output = 0 
        l = 0
        for i,c in enumerate(s): 
            char[c]= char.get(c,0)+1
            while (i-l+1) - max(char.values())>k : 
                char[s[l]]-=1
                l+=1
            output = max(output, i-l+1)
        return output
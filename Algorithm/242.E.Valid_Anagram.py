class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hash 77ms 52.31 % faster / 14.5 mb less than 67.21 %
        hs = {}
        ht = {}
        
        for c in s : 
            if(c not in hs) : 
                hs[c] = 1
            else : 
                hs[c] +=1
        
        
        for c in t : 
            if(c not in ht) : 
                ht[c] = 1
            else : 
                ht[c] +=1
        
        if(hs == ht) : return True
        else : return False
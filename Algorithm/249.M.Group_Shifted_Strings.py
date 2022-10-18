class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        #hash map 74ms 39.41% , 13.8mb less than 98.94
        hm  = {}
        for s in strings :
            key = ''
            for c in range(len(s)-1) : 
                key+=chr((ord(s[c+1])-ord(s[c]))%26+ord('a'))
            if key in hm : hm[key].append(s)
            else : hm[key] = [s]
        return hm.values()
                
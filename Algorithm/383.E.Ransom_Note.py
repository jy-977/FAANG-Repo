class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #problem analysis 
        #1) 문자열 조합
        #2) magazine이 ransomNote의 구성성분을 포함하고있으면 true
        
        #hashtable : 75ms 69.40% faster / 14.2 mb 53.09 less
        hm ={}
        ms = set(magazine)
        for s in ms :
            hm [s] = magazine.count(s)
        for s in  set(ransomNote) : 
            if(s not in ms or hm[s]<ransomNote.count(s)):
                return False
        return True
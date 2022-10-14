class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
       #HASHMAP
#         hm = {}
#         for i in range(len(s)) : 
#             if(s[i] in target) : 
#                 if (s[i] in hm) : 
#                     hm[s[i]]+=1
#                 else : 
#                     hm[s[i]] = 1
#         tm ={}
#         for i in range(len(target)) : 
#             if (target[i] in tm) : 
#                 tm[target[i]]+=1
#             else : 
#                 tm[target[i]] = 1
#         if(len(hm) == len(tm)) : 

#             for a in tm : 
#                 hm[a] //= tm[a]
#             return min(hm.values())
#         else : return 0
#  45ms 71.51% / 13.8 66.39% 
        hm = Counter(s)
        tm = Counter(target)
        for i in tm :
            if i in hm : 
                tm[i] = hm[i] // tm[i]
            else : 
                tm[i] = 0
        return min(tm.values())
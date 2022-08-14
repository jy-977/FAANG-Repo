class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         problem analysis
        # set? hashtable
    
        
# 1) PROBLEM UNDERSTANDING
    #같은 문자열 set을 가지는 단어끼리 묶어서 return 
    #순서는 상관없다
# 2) HINT CHECK
    #big range  : hashpable
    
        
#IDEA 1 : HASH TABLE & set
#solution : IDEA1에서 SET을 제거하면 됨 : 88MS 99.75 FASTER / 17MB LESS THAN 99.03%
        
#         hashmap = {}
#         for str in strs : 
            
#             s = set(str)
#             s = ''.join(sorted(list(s)))
#             print("key : ",s)
            
#             if(s in hashmap) :  
#                 hashmap[s].append(str)
#             else : 
#                 hashmap[s] = [str]
                
#             print(hashmap)
#         print(list(hashmap.values()))
#         return list(hashmap.values())
#       'dddddg','ggggd'같은 경우를 고려하지 못함
#       set을 빼면 답이 된다...  (solution 참고)

# -------------------------------------------            

 #IDEA 2 : HASH TABLE + ORD  
#HASH 만드는 걸 안겹치게 하기 위해서 ORD(C)*ORD(C) 로 했는데 필연적으로 겹칠수 밖에 없음...
#SOLUTION : KEY를 HASHTABLE로만듦 
#142ms 66.92% faster / 18.9mb 34.02% less

        
        hashmap = {}
        for str in strs :
            offset = 1
            # key = 0 
            key = [0] *26
            for c in str:
#                 key+=ord(c)*ord(c)
                key[ord(c)- ord('a')]+=1 # ==> hash table에서 자주 쓰이는 구문임 외우자
            if(tuple(key) in hashmap) :  
                hashmap[tuple(key)].append(str)
            else : 
                hashmap[tuple(key)] = [str]
                
        return list(hashmap.values())
            

        
# key[ord(c)-ord('a')]+=1
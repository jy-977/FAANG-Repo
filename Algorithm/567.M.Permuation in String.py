from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
    
        
#   problem analysis
# 1. permutation : 문법모름
# 2. O()??


# idea 1 : set
#         sett = set(s1)
#         flag = False
        
#         for s in s2 : 
#             if(s in sett) :
#                 if(flag == True) : return True;
#                 flag = True;
#                 sett.remove(s)
#             else : 
#                 if(flag == True) :
# #                   initialize again
#                     flag = False;
#                     sett = set(1)
#         return False;
# 안됨 순열의 길이가 s1과 같은것만 되는거였는데 나는 부분순열도 되는줄 알고 이렇게 짰다...

# idea 2 : two pointers 
# 복잡하다

# idea 3 : sliding window 5932 ms
            length = len(s1)
            pointer =0 
            sorted_s1 = sorted(s1)
            while(pointer<len(s2)-length+1):
                if(s2[pointer] in s1) : 
#                     pemutation check
                    if(sorted(s2[pointer:pointer+length]) == sorted_s1 ) : return True
                pointer += 1

#sliding window 접근방법은 좋은데 구현이 잘못됐다.


# 시간단축포인트 
# 1) sliding window 구현
# 2) 문자열 대신 ord()를 이요해 숫자로 다룸 

# idea 4 : advanced sliding window + hasing 
                A = [ord(x) - ord('a') for x in s1]
                B = [ord(x) - ord('a') for x in s2]

                target = [0] * 26
                for x in A:
                    target[x] += 1

                window = [0] * 26
                for i, x in enumerate(B):
                    print(window)
                    window[x] += 1
                    if i >= len(A):
                        window[B[i - len(A)]] -= 1
                    if window == target:
                        return True
                return False
 
            
            
#content1
# sliding window & two pointer 차이
# sliding window : 고정길이
# two pointers : 연속적, 가변길이
                
                

#content2
# <permutation> : 순열 
# (1,2) is not (2,1)
# from itertools import permutations
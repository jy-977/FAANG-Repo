class Solution(object):
        
        
#   IDEA 1        
#         a ,b= len(s)-1,len(t)-1
#         cntA = cntB =0
        
#         while(a>=0 or b>=0) :
            
#             while(a>=0 and (cntA!=0 or s[a] =='#')) :
#                 if(s[a] =='#') : 
#                     cntA+=1
#                 else :
#                     if( cntA!=0 ) :
#                         cntA-=1
#                 a-=1
#             while(b>=0 and ( cntB!=0 or t[b] =='#')) : 
#                 if(t[b] =='#') : 
#                     cntB+=1
#                 else :
#                     if( cntB!=0 ) :
#                         cntB-=1
#                 b-=1
#             #비교포인트
#             if(a>=0 and b>=0) : 
#                 if(s[a]!=t[b]) : 
#                     return False
#             else : 
#                 if(a==-1 and b==-1) : return True
#                 return False
#             a-=1
#             b-=1     
        
#         # IDEA2 )   solution code  : 46MS ( 59.30% FASTER)  / 13.9MB (74.69 LESS)
        
#         def func(s) : 
#             skip=0
#             for a in reversed(s) : 
#                 if(a =='#') : skip+=1
#                 elif(skip) : skip-=1
#                 else : 
#                     yield a         # yeild? return 하지만 계속 작업을 이어감
#         return all(x==y for x, y in itertools.zip_longest(func(s), func(t)))
    
# #     #새로운 함수 
# #     #yeild
# #     #all
# #     #zip_longest  : zip 인데 길이가 다를때 짧은쪽을 기준으로 묶어줌
# #             (1,2,3) (5,6,7,8) ==> (1,5) (2,6) (3,7)
# #     #zip : (1,2,3) (4,5,6) ==> (1,4) (2,5) (3,6) 이렇게 묶어줌    

# # 이 경우 TIME COMPLEXITY : O(M+N) // SPACE COMPLEXITY : O(1)
# # 내 아이디어 보다 느림


# IDEA 3 : DISCUSS CODE 

    def backspaceCompare(self, S, T):
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1
            
    #내 코드랑 진짜 소름돋게 똑같음.. 
    # while(True) 쓰는걸 두려워하지 말기
    # if( 조건 깔끔하게 하는거 배워야함.. ㅠ)
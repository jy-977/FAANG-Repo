class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #problem analysis
        
        #1) time : O(n) ==> binary search O(logn) , twopointers
        #2) space : O(1) ===> stack X
        #2) short range 
    
        #IDEA 1 ) two pointers  : 39MS (77.92 FASTER ) 14.1MB (LESS THAN 24.7%)
        a ,b= len(s)-1,len(t)-1
        cntA = cntB =0
        
        while(a>=0 or b>=0) :
            
            while(a>=0 and (cntA!=0 or s[a] =='#')) :
                if(s[a] =='#') : 
                    cntA+=1
                else :
                    if( cntA!=0 ) :
                        cntA-=1
                a-=1
            while(b>=0 and ( cntB!=0 or t[b] =='#')) : 
                if(t[b] =='#') : 
                    cntB+=1
                else :
                    if( cntB!=0 ) :
                        cntB-=1
                b-=1
            #비교포인트
            if(a>=0 and b>=0) : 
                if(s[a]!=t[b]) : 
                    return False
            else : 
                if(a==-1 and b==-1) : return True
                return False
            a-=1
            b-=1
        return True

#풀긴 풀었는데 코드가 상당히 더럽다
#항상 맨 끝 , 맨 앞에서 INDEX를 조정하는게 시간에 굉장히 오래걸린다
#이번 코드도 비교 포인트에서 시간이 꽤 오래 걸렸음
#--> while 대신 for을 이용하면 훨씬 수월한경우가 많다

#또 SUBMIT 전에 TESTCASE로는 완벽하게 SUBMIT ACCEPT가 안된다
#이게 어려운 부분중 하나인듯
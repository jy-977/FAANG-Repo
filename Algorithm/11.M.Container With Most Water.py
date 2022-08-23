class Solution:
    def maxArea(self, height: List[int]) -> int:
        #problem analy 
        #1) big range : n ==> bitmasking , two pointer, 
        #2) 
        
    
    #IDEA 1) two pointers (1554ms 9.29% faster / 27.4 mb 85.10% less)
    
        L,R = 0, len(height)-1
        output = 0
        while(L<R):
            output = max(output, min(height[L],height[R])*(R-L))
            if(height[L]<height[R]): 
                L+=1
            else : 
                R-=1
        return output
    
        #옛날에 못풀고 넘어갔던 42.Trapping Rain Water 와 매우 흡사한 문제
        #if/ else 조건이 이해가 안된다
        #왜 작은쪽을 옮겨?
        #==> 왜냐면 우리는 큰게 필요하니까 
        #필요없는 작은쪽 인덱스는 옮긴다
        
        # 최적 솔루션인거 같은데 왜 느리지?
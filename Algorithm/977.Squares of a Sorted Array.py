# 문제분석
# 1) Sorting
# 2) O(n)


class Solution:
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
    
# idea 1) 내장함수    
#         파이썬 sorted complexity O(nlogn)
        # return(sorted(list(map(lambda x : x*x,nums))))
    
    
    
# idea 2) two point? 
# 투포인트 (슬라이딩 윈도우) 처음 접하는 문제
# 투포인트 공부하기

    # 해결방법 
    # 1) nums 의 제곱 list --> squared list 만들기
    # 2) squared list sorting (sliding point)
            
        squared = list(map(lambda x: x*x, nums))
        start, end = 0, len(squared)-1
        sorted =[]
        while (start<=end) : 
            if (squared[start]<squared[end]) : 
                sorted.insert(0,squared[end])
                end= end-1
            else : 
                sorted.insert(0,squared[start])
                start=start+1
        return sorted

# 대체가능 코드 
# insert대신에 sorted를 len(num)만큼 미리 할당해줌
# 이때 sorted =[None] * len(num)이 sorted=[Nome for _ in nums]보다 10배빠르다




# idea 3) two point + abs
# 솔루션 보고 공부한거

    # 
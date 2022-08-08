class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        
        
        
# bit operation / bit manipulation
# 기본 공식 알기
# 1) 최하위비트 : x&-x
# 2) 11111 : 1<<n
# 3) X 번째 비트에 1추가 N|=(1<<X)
# 4) X 번째 비트 0으로 설정  N&=~(1<<X)
# 3-1) X번째 비트에 값이 1인지 확인 : N&(1<<X) 
# 4-1) X번째 비트를 반대값으로 변경 : N^=(1<<X)

 
# idea 1 ) 2의 보수법 55ms / 13.9mb
        if(n==0) : 
            return False
        return (n&-n)==n
# -x = ~x + 1


# idea 2) 1의 보수법
# x & (x-1) 

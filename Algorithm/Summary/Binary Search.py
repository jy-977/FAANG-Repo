#Binary 문제유형
1) O(logn), Sorted arrary 
2) 시간당 용량 계산할때

문제유형 1-1)  기본 + target있을때

l, r = 0, len(arry)-1
while l<=r : 
    mid = (l+r)//2
    if arr[mid] == target : return 
    elif arr[mid] <target : 
        l = mid +1
    else : 
        r = mid-1

문제유형 1-2) 기본 + l==r  
while l<=r : 
    mid = l+ (r-l)//2
    if arr[l] == arr[r] :
        return arr[l]
    elif 조건 1

문제유형 2) 용량 / 시간
    def availble(capacity) :
        summ = 0 
        for a in arr : 
            summ+=math.ceil(a//capacity)
        if summ<=hour : 
            return True
        else : return False
    
    l, r = 최소 용량, 최대용량
    while l<=r : 
        mid = (l+r)//2
        if available(mid) : 
            r = mid -1
        else : 
            l = mid 
    return l
        
        
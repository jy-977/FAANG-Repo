# 쉬움 슬라이딩 윈도우 / 투포인터
#1) sorting
# 2) two pointer

arr.sort()
l ,r = 0, 0
output = 0
while r<len(arr): 
    if arr[r]-arr[l]>k : 
        output+=1
        l = r

    

return output if output >3 else  3
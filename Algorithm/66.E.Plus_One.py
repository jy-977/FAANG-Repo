from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        upper= 0
        digits = deque(digits)
        for i in range(len(digits)-1, -1,-1) :
            if i == len(digits)-1:
                newnum = digits[i]+1
            else : newnum = (digits[i]+upper)
            digits[i] = newnum%10
            upper = 1 if newnum >=10 else 0 
        if upper: 
            digits.appendleft(1)
            
        return digits

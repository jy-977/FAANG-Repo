from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
#         problem analysis
#       1. string
#       2. stack
#       3. O(n)

# idea1 : queue (144ms, 14.1mb)
# 문자열 반환할 필요 없으니 max_length 만 기억
# 문자열안에 포함된 문자가 나오면 length 비교 ==> deque
        
        sub =deque([]);
        max_len = 0;
        for a in s : 
            while (a in sub) :
                if(len(sub)> max_len) : 
                    max_len= len(sub)
                sub.popleft()
            sub.append(a)
        if(len(sub)> max_len) : 
            max_len= len(sub)
        return max_len
                

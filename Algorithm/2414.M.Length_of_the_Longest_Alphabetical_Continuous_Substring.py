class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        #requirement
        #가장 긴 연속 문자열 길이 반환

        #analysis
        #10^5 ==> o(N) : hashmap, set , twopointer, bit manipulation, KMP

        #idea : twopointer
        #18분.. 정도걸림
        #runtime : 1174ms(41.63 faster) O(n)
        #memory : 14.9mb (95.6 less)
        if len(s)<2 : 
            return 1

        l=0
        longest = 0
        while l<len(s):
            long = 0
            while l+long<len(s) and ord(s[l+long]) == ord(s[l])+long : 
                long+=1
            longest = max(longest, long)
            l= l+long
        return longest
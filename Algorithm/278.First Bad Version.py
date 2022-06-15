# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        version = list(range(1,n+1))
        
        bad = n+1
        while len(version)>1:
            length = len(version)
            print(version)
            if isBadVersion(version[int(length/2)])== True: 
                if version[int(length/2)]<bad : 
                     bad = version[int(length/2)]
                        
#           right
            if isBadVersion(version[int(length/2)])== False : 
                print("right", bad)
                version = version[int(length/2)+1:]         
                
#           left
            else: 
                print("left",bad)
                version = version [:int(length/2)]
                
        if isBadVersion(version[0]) :return version[0]
        else : return bad
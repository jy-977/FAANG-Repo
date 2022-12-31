# Runtime
# 91 ms
# Beats
# 98.99%
# Memory
# 15.1 MB
# Beats
# 94.52%

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #requirment
        # return asteroids list after collision
        # number : size, -/+ : direction

        #analysis
            #O(nlogn), 2 <= asteroids.length <= 10^4


        #tip 
        #pop 되는 경우만 정의 
        #나머지는 다 append

   
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans


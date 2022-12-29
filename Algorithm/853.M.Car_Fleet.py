class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #requirement
            #추월 안됨
            #앞차보다 빠르면 앞차 속도에 맞
            #fleet : 자동차의 무리

        #analysis
            #O(n) : 1 <= n <= 105
            # monotonic stack, bit manipulation, set, hashmap, twopointers

            #--> 아니고 nlogn 이었음
        # Runtime 950 ms
        # Beats 91.31%
        # Memory 32.1 MB
        # Beats 98.9%

        cars = [(p,s) for p,s in zip(position, speed)]
        stack = []

        for p,s in sorted(cars)[::-1] : 
            time =(target-p) /s 
            if not stack or time>stack[-1] : 
                stack.append(time)
        return len(stack)
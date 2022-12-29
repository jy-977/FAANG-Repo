# stack 

# monotonic stack 단조스택
- time complexity O(n),
- space complexcity O(n)
- 이 알고리즘을 생각해내는건 어려우니 외우자

- definition : 스택의 순서를 오름차순 / 내림차순으로 유지
- 각 element보다 큰값 / 작은값 의 상대적인 위치를 이용하는 문제에 유용
- problems : 

        739, 42, 853

- technique : 

        1. stack[-1] 와 arr[i]를 비교
        2. while stack[-1]< arr[i] : stack.pop ()
        3. stack.append(arr[i]) 


- code : 

        output = []*len(arr)
        stack = []  # pair : [val, i]

        for i, val in enumerate(arr) : 
            while stack and val> stack[-1][0] : # stack[-1][0] 스택 맨 마지막의 [-1]      값 [0] 
                s_val , s_idx = stack.pop()
                output[idx] = ...   
            stack.append([val, i])
        return output

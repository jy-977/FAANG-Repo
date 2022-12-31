class Solution:
    def countCollisions(self, directions: str) -> int:
        #requiement 
        #return number of collision (충돌)
        #동시에 와서 박으면 +2
        #하나가 와서 박으면 +1
        

        #analysis
        # O(n) : 1<=n <=10^5
        # O(n) : two pointers, dp , set, bit manipulation, hashmap, monotonic stack
        
        #idea : monotonic stack
        #condition
        # LR : break 
        # RL : +2
        # RS, SL : +1
        # hm = {'R': 1, 'L' :-1 , 'S' : 0}
        # output = 0
        # numD = []
        # # generate numD 
        # for i,num in enumerate(directions) : 
        #     if i>1 and directions[i-1] == num : 
        #         numD.append(numD[-1])
        #     else : 
        #         numD.append(i+hm[num])
        # print(numD)

        #calculate total collision

        # for i,d in enumerate(numD) : 
        #     if 


        
        # return 0 


        #solution
            #직관...!
            #맨 왼쪽L, 맨 오른쪽 R, S 의 개수를 뺀게 답
            #Runtime 171 ms
            # Beats  87.55%
            # Memory 15 MB
            # Beats 70.4%
        length = len(directions)
        i,j = 0,length-1

        while i<length: 
            if directions[i] != 'L' :  
                break 
            i+=1
        l = i
        while 0<=j: 
            if directions[j] != 'R' :  
                break 
            j-=1
        r = j
        output=0
        for i in range(l,r+1) : 
            if directions[i]=='S' : 
                continue
            output+=1
        return output
        
        #태그에는 stack이라고 되어 있는데 stack 어떻게 쓰는지 모르겠다..
        #이건 simulation 아닌가
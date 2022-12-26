class Solution:
    def countAndSay(self, n: int) -> str:
        #requirement
        #countAndSay 함수 작성
        #countAndSay : n개의 숫자s 가 연속적으로 나옴 return "ns"

        #Analysys
        #recursive / stack /dp

        #idea 1 : dp 
        #25.30초
        #46ms 91.25% faster / 13.9mb 56.2% less

        memory =[0 for i in range(n)]

        for i in range(n) : 
            if i == 0 : 
                memory[i] = "1"
            else : 
                #countAndSay 
                s = memory[i-1]
                news = ""
                idx= 0
                while idx<len(s) : 
                    cnt =1
                    while (len(s)>idx+1 and s[idx]==s[idx+1]) :
                        cnt+=1
                        idx+=1
                    news += str(cnt)+s[idx]
                    idx +=1
                memory[i] = news
        return memory[n-1]
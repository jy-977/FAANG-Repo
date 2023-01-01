class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        #requirement 
            # if mass>= asteroids[i] : 
            #     mass+= asteroid[i]
            #     asteroid[i]=0
            # else :
            #     asteroid[i]+=mass 
            #     mass =0
            
            #return True, False // 행성 다 부실수 있는지 
            # arbitrary order : 임의의 순서!!!

        #analysis
        # 1 <= asteroids.length <= 105
        # O(nlogn)
        
    #    Runtime 1206 ms
    #     Beats 67.56%
    #     Memory 25.5 MB
    #     Beats 89.1%


        asteroids.sort()
        for i in range(len(asteroids)) : 
            if mass>= asteroids[i] : 
                mass+= asteroids[i]
                asteroids[i]=0
            else :
                return False
        return True


        #idea 
      
      #solution... 
      Greedy라네.. 아직 greedy에 대한 개념이 약한듯
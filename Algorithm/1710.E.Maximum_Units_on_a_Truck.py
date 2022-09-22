class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        #problem analysis
        #range : middle?
        
        #문제 이해 : 
        # sum (boxtype[i][0] ) = 10
        # output = max( sum (boxtype[i][0] * ))
        
 #idea 1) sort : 391ms faster 20.69% , 14.4 mb 82.71% less==================================================
        # boxTypes[][1]을 기준으로 정렬
        # boxTypes.sort(key = lambda x : x[1] ,reverse=True)
        # boxSum =0
        # units =0
        # for i in range(len(boxTypes)) : 
        #     if(boxSum>=truckSize) : 
        #         return units
        #     if(boxTypes[i][0]<truckSize-boxSum) : 
        #         units += boxTypes[i][0]*boxTypes[i][1]
        #         boxSum += boxTypes[i][0]
        #     else :
        #         units += (truckSize-boxSum)*boxTypes[i][1]
        #         boxSum += truckSize-boxSum
        # return units

#===================================================================
#         #edge case : 
        
#         #1) same capacity 여러개
#         [5,10], [2,5], [4,7] , [1,10] truck size 10 
        
#         #2) 길이 sum(boxnumber)< trucksize
#         [1,10], [4,8] truck size 10
        
#         #3) empty boxtype 
#         [][]
#========================================================================================================
#         파이썬 정렬 기준
#         list.sort(key , reverse|)

        
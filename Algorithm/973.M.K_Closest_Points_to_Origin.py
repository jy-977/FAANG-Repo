class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point) : 
            return  pow(point[0],2)+pow(point[1],2)

# idea 1) hashmap 
#         hm = {}
#         for i in range(len(points)) :
#             hm [i] =  distance(points[i])
#         shm = (sorted(hm.items() , key = lambda item : item[1], reverse = False))
#         print(shm)
#         out = []
#         for i in range(k) : 
#             out.append(points[shm[i][0]])
            
#         return out

# idea 2) list : 181ms 98.04 faster / 20.3mb 61.82 less
#         hm = []
#         for point in points:
#             hm.append((point,distance(point)) )
#         hm.sort(key = lambda x : x[1], reverse=False)
#         out =[]
#         for i in range(k) : 
#             out.append(hm[i][0])
        
#         return out

# idea 3 : 911ms 85.17% 20.3mb 61.82
        points.sort(key = lambda x : x[0]*x[0]+x[1]*x[1])
        return points[:k]
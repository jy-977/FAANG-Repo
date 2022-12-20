#Union Find 


#Graph #서로소집합 #Disjoint-Set

#간단 순서 
#1. Parent 배열 선언 
parent = [i for i in range(n)]

# 2. Find 함수
def find (x) :
    if parent[x] == x : return x
    else : 
        parent[x] = find(parent[x])
        return parent[x]

#3.Union 함수 
def union (x,y) : 
    a = find(x)
    b = find(y)
    #2값이 더 작은 쪽으로
    if (x>y) : parent[x] = y
    else: parent[y] = x 

#4.판별

if find(x)==find(y) : return True
else : return False

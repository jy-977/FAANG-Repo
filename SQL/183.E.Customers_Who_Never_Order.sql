# Write your MySQL query statement below

#idea 1) not in 

# select *
# from Customers as c , Orders as o
# where c.id not in (select CustomerId from Orders as o )
#이렇게 하면 결과가 다음과 가다
# id  name   id    customerID
#------------------------------
# 2   henry   2   1
# 2   henry   1   3
# 4   max     2   1
# 4   max     1   3
#즉 쓸데 없는 테이블 from 으로 불러들이면 
# select * from customer where id not in (select customerID from Orders as o )
# 한 결과값에 Orders의 모든 열이 X(곱셈)된다


#solution : 771ms 31.62% , 0B 100.00% 

select name as Customers
from Customers as c 
where c.id not in (select CustomerId from Orders as o )


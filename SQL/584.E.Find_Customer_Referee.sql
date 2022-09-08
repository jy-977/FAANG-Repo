# Write your MySQL query statement below
#542ms 57.28% faster / 0B 100% faster
select name
from Customer
where referee_id != 2 or referee_id is Null

#1) id!=2 할때 null check 안함
#2) my sql에서 != 과 <>은 같다
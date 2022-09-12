# Write your MySQL query statement below
#448ms 73.22% , 0B 100.00%
select sell_date, count(distinct product) as num_sold , group_concat(distinct product order by product) as products
from activities
group by sell_date



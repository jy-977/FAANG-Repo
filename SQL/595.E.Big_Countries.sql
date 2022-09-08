# Write your MySQL query statement below
#498ms (12.11% faster) 0B 100% faster
select name, population, area
from World
where area>=3000000 or population >=25000000
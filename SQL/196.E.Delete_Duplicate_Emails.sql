# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
# 이것도 다 나름의 알고리즘이 필요하구나..

#idea 1) 962m faster than 49.07
# delete P1 from Person p1, Person p2
# where p1.Email = p2.Email and p1.Id> p2.Id


delete from Person where Id not in (select * from (select min(id) from Person group by email)as p)
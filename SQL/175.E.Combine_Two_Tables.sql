# Write your MySQL query statement below
#Join 417ms (65.00%) 0B (100%)


select firstName, lastName , city, state
from Person 
left outer join  Address
on Person.personId = Address.personId
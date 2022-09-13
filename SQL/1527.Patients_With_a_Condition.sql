# Write your MySQL query statement below
#425MS 44.48% FASTER / 0B 100.00% LESS
select patient_id , patient_name , conditions
from Patients 
where conditions like 'DIAB1%' OR conditions LIKE '% DIAB1%'

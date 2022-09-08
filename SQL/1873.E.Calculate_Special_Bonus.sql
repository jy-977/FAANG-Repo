# select E.employee_id , b.bonus
# from Employees as E 
# left outer join (select employee_id,  salary as bonus 
#     from Employees
#     where name not like 'M%' and employee_id%2=1) as b 
# on E.employee_id = b.employee_id
# order by E.Employee_id



#solution : 734ms (45.11% faster) 0B 100% faster
SELECT employee_id,
IF (employee_id%2 AND name not like "M%", salary, 0) as bonus
FROM Employees order by employee_id;

#column 을 if (조건, 참, 거짓) as 이름 으로 지정해줄수 있다


#245MS 67.73% FASTER
# UPDATE Salary
# SET 
#     sex = CASE sex 
#         WHEN 'f' THEN 'm'
#         ELSE 'f'
#     end
    
    

#update table set 조건
#sql 에서도 if, case문 쓸수 있다

#565MS 7.68 FASTER

update Salary set sex= if(sex='m', 'f', 'm')

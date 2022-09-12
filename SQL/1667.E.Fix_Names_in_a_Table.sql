
# Write your MySQL query statement below
# 문자열 쪼개는 함수
#1) left(column, 1) , right(colum(name)-1)
#2) substr(str, 시작,몇개) // substr(str, 시작) --> 이경우 끝까지 
#3) concat(문자1, 문자열2) 문자열합치기


#1150ms , 15.25% faster
# select user_id, concat(Upper(substr(name,1,1)),Lower(substr(name,2))) as name
# from Users
# order by user_id



#803ms , 44.18% faster
select user_id, concat(Upper(left(Users.name,1)),Lower(right(Users.name,length(name)-1))) as name
from Users
order by user_id


# Write your MySQL query statement below
select query_name, round(avg(rating/position), 2) as quality, ROUND(AVG(CASE WHEN rating < 3 THEN 1.0 ELSE 0.0 END) * 100, 2) as poor_query_percentage
from queries
group by query_name
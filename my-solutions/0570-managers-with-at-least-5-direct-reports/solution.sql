# Write your MySQL query statement below
SELECT m.name
FROM Employee m
LEFT JOIN Employee e ON m.id = e.managerId
GROUP BY m.id
HAVING COUNT(*) >= 5;

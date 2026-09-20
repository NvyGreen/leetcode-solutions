# Write your MySQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1, Logs l2, Logs l3
WHERE l2.id + 1 = l1.id
    AND l2.num = l1.num
    AND l3.id - 1 = l1.id
    AND l3.num = l1.num;

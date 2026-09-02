# Write your MySQL query statement below
SELECT 
    (
        CASE
            WHEN MOD(s.id, 2) = 1 AND s.id = q.counts THEN s.id
            WHEN MOD(s.id, 2) = 1 AND s.id <> q.counts THEN s.id + 1
            ELSE s.id - 1
        END
    ) as id,
    s.student
FROM Seat s
JOIN (
    SELECT COUNT(*) AS counts FROM Seat
) q
ORDER BY id;

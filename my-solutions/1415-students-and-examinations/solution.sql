# Write your MySQL query statement below
SELECT t.student_id, t.student_name, s.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students t
CROSS JOIN Subjects s
LEFT JOIN Examinations e
    ON e.student_id = t.student_id
    AND e.subject_name = s.subject_name
GROUP BY t.student_id, t.student_name, s.subject_name
ORDER BY t.student_id, s.subject_name;

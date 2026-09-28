# Write your MySQL query statement below
SELECT
    user_id,
    user_name,
    credit + paid + receive AS credit,
    CASE WHEN
        credit + paid + receive > 0 THEN 'No'
        ELSE 'Yes'
    END AS credit_limit_breached
FROM (
    SELECT
        U.user_id,
        U.user_name,
        U.credit,
        SUM(CASE WHEN U.user_id = T.paid_by THEN -amount ELSE 0 END) AS paid,
        SUM(CASE WHEN U.user_id = T.paid_to THEN amount ELSE 0 END) AS receive
    FROM Users U
    LEFT OUTER JOIN Transactions T
    ON U.user_id = T.paid_by OR U.user_id = T.paid_to
    GROUP BY U.user_id, U.user_name
) TMP
ORDER BY user_id;

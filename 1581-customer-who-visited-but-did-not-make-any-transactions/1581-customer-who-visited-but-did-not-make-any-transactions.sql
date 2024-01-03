# Write your MySQL query statement below

SELECT customer_id, COUNT(customer_id) as count_no_trans
FROM
    (SELECT v.customer_id AS customer_id, t.transaction_id as tid
    FROM Visits v
    LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id) AS nt
WHERE tid IS NULL
GROUP BY customer_id;

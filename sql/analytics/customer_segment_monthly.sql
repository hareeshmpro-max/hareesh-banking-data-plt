SELECT
    DATE_TRUNC('month', f.transaction_date) AS month,
    c.customer_segment,
    COUNT(*) AS transaction_count,
    SUM(f.amount) AS transaction_amount
FROM fact_transaction f
JOIN dim_customer c
  ON f.customer_id = c.customer_id
WHERE f.status = 'SUCCESS'
GROUP BY 1, 2
ORDER BY 1, 2;

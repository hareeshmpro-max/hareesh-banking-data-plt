SELECT
    DATE_TRUNC('month', transaction_date) AS month,
    COUNT(*) AS transaction_count,
    SUM(amount) AS transaction_amount
FROM fact_transaction
WHERE status = 'SUCCESS'
GROUP BY 1
ORDER BY 1;

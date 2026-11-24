SELECT
    DATE_TRUNC('month', loan_date) AS month,
    SUM(loan_amount) AS active_loan_amount,
    AVG(interest_rate) AS average_interest_rate
FROM fact_loan
WHERE loan_status = 'ACTIVE'
GROUP BY 1
ORDER BY 1;

-- Source-to-target reconciliation
-- Apply the same business rules on both sides.

-- SOURCE: valid transactions
SELECT
    COUNT(*) AS transaction_count,
    SUM(t.amount) AS transaction_amount
FROM stg_transactions t
JOIN dim_account a
    ON t.account_id = a.account_id
WHERE t.status = 'SUCCESS'
  AND t.amount > 0;


-- TARGET: valid analytics transactions
SELECT
    COUNT(*) AS transaction_count,
    SUM(amount) AS transaction_amount
FROM fact_transaction
WHERE status = 'SUCCESS'
  AND amount > 0;
-- Source-to-target reconciliation pattern

SELECT
    COUNT(*) AS transaction_count,
    SUM(amount) AS transaction_amount
FROM stg_transactions
WHERE status = 'SUCCESS'
  AND amount > 0;

SELECT
    COUNT(*) AS transaction_count,
    SUM(amount) AS transaction_amount
FROM fact_transaction
WHERE status = 'SUCCESS';

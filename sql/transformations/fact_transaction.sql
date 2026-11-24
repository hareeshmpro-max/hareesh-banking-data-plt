-- Analytics fact logic
SELECT
    t.transaction_id,
    t.account_id,
    a.customer_id,
    t.transaction_date,
    t.transaction_type,
    t.amount,
    t.status
FROM stg_transactions t
JOIN dim_account a
  ON t.account_id = a.account_id
WHERE t.status = 'SUCCESS'
  AND t.amount > 0;

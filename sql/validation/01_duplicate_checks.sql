-- Find duplicate transaction business keys
SELECT transaction_id, COUNT(*) AS record_count
FROM stg_transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;

-- Find transactions referencing missing accounts
SELECT t.*
FROM stg_transactions t
LEFT JOIN dim_account a
  ON t.account_id = a.account_id
WHERE a.account_id IS NULL;

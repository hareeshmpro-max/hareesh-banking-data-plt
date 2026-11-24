-- Staging view/table logic
SELECT
    transaction_id,
    account_id,
    CAST(transaction_date AS DATE) AS transaction_date,
    UPPER(transaction_type) AS transaction_type,
    CAST(amount AS DECIMAL(18,2)) AS amount,
    UPPER(status) AS status
FROM raw_transactions;

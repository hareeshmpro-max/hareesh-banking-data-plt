SELECT
    loan_id,
    customer_id,
    loan_type,
    loan_amount,
    interest_rate,
    loan_status,
    loan_date
FROM stg_loans
WHERE loan_amount > 0
  AND loan_status IN ('ACTIVE', 'CLOSED');

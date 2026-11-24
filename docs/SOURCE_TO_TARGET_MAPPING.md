# Source-to-Target Mapping

| Source | Target | Rule |
|---|---|---|
| customers.customer_id | dim_customer.customer_id | Direct |
| customers.customer_name | dim_customer.customer_name | Direct |
| customers.customer_segment | dim_customer.customer_segment | Direct |
| accounts.account_id | dim_account.account_id | Direct |
| accounts.customer_id | dim_account.customer_id | Foreign key |
| transactions.transaction_id | fact_transaction.transaction_id | Direct |
| transactions.account_id | fact_transaction.account_id | Join to dim_account |
| transactions.transaction_date | fact_transaction.date_key | Convert to date key |
| transactions.amount | fact_transaction.amount | Positive valid amounts only |
| loans.loan_id | fact_loan.loan_id | Direct |
| loans.loan_amount | fact_loan.loan_amount | Positive values only |

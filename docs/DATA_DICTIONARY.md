# Data Dictionary

## customers
- customer_id: business key
- customer_name: customer display name
- gender: customer gender code
- city: registered city
- customer_segment: Premium / Standard
- registration_date: registration date

## accounts
- account_id: business key
- customer_id: customer foreign key
- account_type: SAVINGS / CURRENT
- opening_date: account opening date
- balance: current account balance
- status: account status

## transactions
- transaction_id: business key
- account_id: account foreign key
- transaction_date: transaction date
- transaction_type: CREDIT / DEBIT
- amount: transaction amount
- status: SUCCESS / FAILED

## loans
- loan_id: business key
- customer_id: customer foreign key
- loan_type: HOME / PERSONAL / AUTO
- loan_amount: principal amount
- interest_rate: annual interest rate
- loan_status: ACTIVE / CLOSED
- loan_date: loan origination date

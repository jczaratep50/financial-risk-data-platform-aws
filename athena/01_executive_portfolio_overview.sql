-- Executive Portfolio Overview KPIs
WITH risk_summary AS (
    SELECT 
        loan_id, 
        expected_loss, 
        CASE 
            WHEN default_flag = TRUE THEN 1
            ELSE 0
        END AS default_flag_int
    FROM risk_metrics
)
SELECT 
    COUNT(l.loan_id) AS total_loans, 
    COUNT(DISTINCT l.customer_id) AS total_customers, 
    ROUND(SUM(l.outstanding_balance), 2) AS outstanding_balance,
    ROUND(SUM(COALESCE(dt.expected_loss, 0)), 2) AS expected_loss, 
    ROUND(AVG(l.interest_rate), 2) AS avg_interest_rate, 
    SUM(dt.default_flag_int) AS loans_in_default, 
    ROUND(
        (CAST(SUM(dt.default_flag_int) AS DECIMAL(10, 2)) / COUNT(l.loan_id)) * 100, 2
    ) AS default_rate
FROM loans l
LEFT JOIN risk_summary dt ON l.loan_id = dt.loan_id;
